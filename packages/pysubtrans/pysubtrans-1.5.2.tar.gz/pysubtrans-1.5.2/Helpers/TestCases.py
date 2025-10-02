from copy import deepcopy
from datetime import timedelta
import unittest
from typing import Any

import regex

from PySubtrans.Helpers.Tests import log_test_name
from PySubtrans.Options import Options, SettingsType
from PySubtrans.SettingsType import SettingsType
from PySubtrans.SubtitleBatch import SubtitleBatch
from PySubtrans.SubtitleError import TranslationError
from PySubtrans.SubtitleFileHandler import SubtitleFileHandler
from PySubtrans.SubtitleFormatRegistry import SubtitleFormatRegistry
from PySubtrans.Subtitles import Subtitles
from PySubtrans.SubtitleLine import SubtitleLine
from PySubtrans.SubtitleScene import SubtitleScene
from PySubtrans.Translation import Translation
from PySubtrans.TranslationClient import TranslationClient
from PySubtrans.TranslationPrompt import TranslationPrompt
from PySubtrans.TranslationRequest import TranslationRequest
from PySubtrans.TranslationProvider import TranslationProvider

class LoggedTestCase(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        log_test_name(self._testMethodName)


class SubtitleTestCase(LoggedTestCase):
    def __init__(self, methodName: str = "runTest", custom_options : dict|None = None) -> None:
        super().__init__(methodName)

        options = SettingsType({
            'provider': 'Dummy Provider',
            'provider_settings': { 
                'Dummy Provider' : SettingsType(),
                'Dummy Claude' : SettingsType(),
                'Dummy GPT' : SettingsType()
                },
            'target_language': 'English',
            'scene_threshold': 60.0,
            'min_batch_size': 10,
            'max_batch_size': 20,
            'preprocess_subtitles': False,
            'postprocess_translation': False,
            'project_file': False,
            'retry_on_error': False,
            'stop_on_error': True
        })

        if custom_options:
            options.update(custom_options)

        self.options = Options(options)

        self.assertIn("Dummy Provider", self.options.provider_settings, "Dummy Provider settings should exist")

    def setUp(self) -> None:
        super().setUp()

    def _assert_same_as_reference(self, subtitles : Subtitles, reference_subtitles: Subtitles):
        """
        Assert that the current state of the subtitles is identical to the reference datamodel
        """
        for scene_number in range(1, len(subtitles.scenes) + 1):
            scene = subtitles.GetScene(scene_number)
            reference_scene = reference_subtitles.GetScene(scene_number)

            self._assert_same_as_reference_scene(scene, reference_scene)

    def _assert_same_as_reference_scene(self, scene : SubtitleScene, reference_scene : SubtitleScene):
        self.assertEqual(scene.size, reference_scene.size)
        self.assertEqual(scene.linecount, reference_scene.linecount)
        self.assertEqual(scene.summary, reference_scene.summary)

        for batch_number in range(1, scene.size + 1):
            batch = scene.GetBatch(batch_number)
            reference_batch = reference_scene.GetBatch(batch_number)

            self._assert_same_as_reference_batch(batch, reference_batch)

    def _assert_same_as_reference_batch(self, batch : SubtitleBatch|None, reference_batch : SubtitleBatch|None):
        """
        Assert that the current state of the batch is identical to the reference batch
        """
        self.assertIsNotNone(batch, f"Batch is None")
        self.assertIsNotNone(reference_batch, f"Reference batch is None")

        if batch is None or reference_batch is None:
            return

        self.assertEqual(batch.size, reference_batch.size)
        self.assertEqual(batch.summary, reference_batch.summary)

        self.assertEqual(len(batch.originals), len(reference_batch.originals))
        self.assertEqual(len(batch.translated), len(reference_batch.translated))

        self.assertSequenceEqual([ line.text for line in batch.originals ], [ line.text for line in reference_batch.originals ])
        self.assertSequenceEqual([ line.text for line in batch.translated ], [ line.text for line in reference_batch.translated ])
        self.assertSequenceEqual([ line.start for line in batch.originals ], [ line.start for line in reference_batch.originals ])
        self.assertSequenceEqual([ line.end for line in batch.originals ], [ line.end for line in reference_batch.originals ])


def PrepareSubtitles(subtitle_data : dict, key : str = 'original', file_handler: SubtitleFileHandler|None = None) -> Subtitles:
    """
    Prepares a SubtitleFile object from subtitle data.
    """
    filename = subtitle_data['filename']
    handler = file_handler or SubtitleFormatRegistry.create_handler(filename=filename)
    subtitles: Subtitles = Subtitles()
    subtitles.LoadSubtitlesFromString(subtitle_data[key], file_handler=handler)
    subtitles.UpdateSettings(SettingsType(subtitle_data))
    return subtitles

def AddTranslations(subtitles : Subtitles, subtitle_data : dict, key : str = 'translated'):
    """
    Adds translations to the subtitles.
    """
    translated_file = PrepareSubtitles(subtitle_data, key)
    subtitles.translated = translated_file.originals
    if subtitles.translated is None:
        raise ValueError("No translated subtitles found in the provided data")

    for scene in subtitles.scenes:
        for batch in scene.batches:
            line_numbers = [ line.number for line in batch.originals ]
            batch_translated = [ line for line in subtitles.translated if line.number in line_numbers ]
            batch.translated = batch_translated

            for line in batch.originals:
                line.translated = next((l for l in batch_translated if l.number == line.number), None)
                translated = line.translated
                line.translation = translated.text if translated else None

def AddResponsesFromMap(subtitles : Subtitles, test_data : dict):
    """
    Add translator responses to the subtitles if test_data has a response map.
    """
    for prompt, response_text in test_data.get('response_map', []).items():
        # Find scene and batch number from the prompt, e.g. "Translate scene 1 batch 1"
        re_match : regex.Match|None = regex.match(r"Translate scene (\d+) batch (\d+)", prompt)
        if not re_match:
            raise ValueError(f"Invalid prompt format: {prompt}")
        scene_number = int(re_match.group(1))
        batch_number = int(re_match.group(2))
        batch = subtitles.GetBatch(scene_number, batch_number)
        batch.translation = Translation({'text': response_text})


def BuildSubtitlesFromLineCounts(line_counts : list[list[int]]) -> Subtitles:
    """Generate deterministic subtitles directly from line counts."""

    subtitles = Subtitles()
    if not line_counts:
        return subtitles

    within_batch_gap = timedelta(seconds=1)
    between_batch_gap = timedelta(seconds=2)
    scene_gap = timedelta(seconds=15)
    line_duration = timedelta(seconds=1)

    current_time = timedelta(seconds=0)
    line_number = 1
    scenes : list[SubtitleScene] = []

    for scene_index, batch_counts in enumerate(line_counts, start=1):
        scene = SubtitleScene({'scene': scene_index, 'number': scene_index})
        scene.summary = f"Scene {scene_index}"

        batches : list[SubtitleBatch] = []
        for batch_index, line_count in enumerate(batch_counts, start=1):
            batch_lines : list[SubtitleLine] = []

            for line_offset in range(1, line_count + 1):
                start_time = current_time
                end_time = start_time + line_duration

                batch_lines.append(
                    SubtitleLine.Construct(
                        line_number,
                        start_time,
                        end_time,
                        f"Scene {scene_index} Batch {batch_index} Line {line_offset}"
                    )
                )

                line_number += 1
                current_time = end_time
                if line_offset < line_count:
                    current_time += within_batch_gap

            batches.append(SubtitleBatch({
                'scene': scene_index,
                'number': batch_index,
                'summary': f"Scene {scene_index} Batch {batch_index}",
                'originals': batch_lines
            }))

            if batch_index < len(batch_counts):
                current_time += between_batch_gap

        scene.batches = batches
        scenes.append(scene)

        if scene_index < len(line_counts):
            current_time += scene_gap

    subtitles.scenes = scenes
    return subtitles

class DummyProvider(TranslationProvider):
    name = "Dummy Provider"

    def __init__(self, data : dict):
        super().__init__("Dummy Provider", SettingsType({
            "model": "dummy",
            "data": data,
        }))

    def GetTranslationClient(self, settings : SettingsType) -> TranslationClient:
        client_settings : dict = deepcopy(self.settings)
        client_settings.update(settings)
        return DummyTranslationClient(settings=client_settings)

class DummyClaude(TranslationProvider):
    name = "Dummy Claude"

    def __init__(self, data : dict):
        super().__init__("Dummy Claude", SettingsType({
            "model": "claude-1000-sonnet",
            "data": data,
        }))

class DummyGPT(TranslationProvider):
    name = "Dummy GPT"

    def __init__(self, data : dict):
        super().__init__("Dummy GPT", SettingsType({
            "model": "gpt-5-dummy",
            "data": data,
        }))


class DummyTranslationClient(TranslationClient):
    def __init__(self, settings : SettingsType):
        super().__init__(settings)
        self.data: dict[str, Any] = settings.get('data', {}) # type: ignore[assignment]
        self.response_map: dict[str, str] = self.data.get('response_map', {})

    def BuildTranslationPrompt(self, user_prompt : str, instructions : str, lines : list[SubtitleLine], context : dict) -> TranslationPrompt:
        """
        Validate parameters and generate a basic dummy prompt
        """
        if not instructions:
            raise TranslationError("Translator did not receive instructions")

        if not lines:
            raise TranslationError("Translator did not receive lines")

        if not context:
            raise TranslationError("Translator did not receive context")

        if not context.get('movie_name'):
            raise TranslationError("Translator did not receive movie name")

        if not context.get('description'):
            raise TranslationError("Translator did not receive description")

        names = context.get('names', None)
        if not names:
            raise TranslationError("Translator did not receive name list")

        expected_names = self.data.get('names', [])
        if len(names) < len(expected_names):
            raise TranslationError("Translator did not receive the expected number of names")

        scene_number = context.get('scene_number')
        batch_number = context.get('batch_number')
        user_prompt = f"Translate scene {scene_number} batch {batch_number}"

        prompt = TranslationPrompt(user_prompt, False)
        prompt.prompt_template = "{prompt}"
        prompt.supports_system_prompt = True
        prompt.GenerateMessages(instructions, lines, context)

        return prompt

    def _request_translation(self, request: TranslationRequest, temperature: float|None = None) -> Translation|None:
        for user_prompt, text in self.response_map.items():
            if user_prompt == request.prompt.user_prompt:
                text = text.replace("\\n", "\n")
                return Translation({'text': text})
