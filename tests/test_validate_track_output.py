from __future__ import annotations

import copy
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests.test_validate_playlist_spec import valid_playlist_spec


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_track_output.py"
FIXTURES = ROOT / "tests" / "fixtures"
FENCE = chr(96) * 3
GOLDEN_SPEC = json.loads(
    (FIXTURES / "track-01-spec.json").read_text(encoding="utf-8")
)
GOLDEN_OUTPUT = (FIXTURES / "track-01-output.md").read_text(encoding="utf-8")
MAIN_FIELDS = (
    "Style",
    "Feel",
    "Tempo/Groove",
    "Vocal",
    "Instrumentation",
    "Harmony",
    "Form/Flow",
    "Production/Mix",
)


def compile_main(spec: dict[str, object]) -> str:
    fields = spec["prompt_fields"]
    assert isinstance(fields, dict)
    return " ".join(f"{name}: {fields[name]}" for name in MAIN_FIELDS)


def golden_lyrics() -> str:
    match = re.search(
        rf"(?ms)^\*\*가사\*\*\s*\n{re.escape(FENCE)}text\s*\n"
        rf"(.*?)\n{re.escape(FENCE)}\s*$",
        GOLDEN_OUTPUT,
    )
    assert match
    return match.group(1)


def render_output(spec: dict[str, object], lyrics: str | None = None) -> str:
    return f"""**기본프롬프트**
{FENCE}text
{compile_main(spec)}
{FENCE}

**절대불가프롬프트**
{FENCE}text
{spec["exclusion_prompt"]}
{FENCE}

### {spec["title"]}

**가사**
{FENCE}text
{lyrics if lyrics is not None else golden_lyrics()}
{FENCE}
"""


def bound_track_lyrics() -> str:
    lines = "\n".join("조용한밤길따라" for _ in range(12))
    return f"[Intro]\n\n[Verse]\n{lines}\n\n[Outro]"


class TrackOutputValidatorTests(unittest.TestCase):
    def run_validator(
        self,
        text: str,
        spec: dict[str, object] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        with (
            tempfile.NamedTemporaryFile(
                "w", encoding="utf-8", suffix=".md"
            ) as output_handle,
            tempfile.NamedTemporaryFile(
                "w", encoding="utf-8", suffix=".json"
            ) as spec_handle,
        ):
            output_handle.write(text)
            output_handle.flush()
            json.dump(spec or GOLDEN_SPEC, spec_handle, ensure_ascii=False)
            spec_handle.flush()
            return subprocess.run(
                [
                    sys.executable,
                    str(VALIDATOR),
                    output_handle.name,
                    "--spec",
                    spec_handle.name,
                ],
                capture_output=True,
                check=False,
                text=True,
            )

    def run_playlist_validator(
        self,
        text: str,
        catalog: dict[str, object],
        playlist: dict[str, object],
        track: int = 1,
    ) -> subprocess.CompletedProcess[str]:
        with (
            tempfile.NamedTemporaryFile(
                "w", encoding="utf-8", suffix=".md"
            ) as output_handle,
            tempfile.NamedTemporaryFile(
                "w", encoding="utf-8", suffix=".json"
            ) as playlist_handle,
            tempfile.NamedTemporaryFile(
                "w", encoding="utf-8", suffix=".json"
            ) as catalog_handle,
        ):
            output_handle.write(text)
            output_handle.flush()
            json.dump(playlist, playlist_handle, ensure_ascii=False)
            playlist_handle.flush()
            json.dump(catalog, catalog_handle, ensure_ascii=False)
            catalog_handle.flush()
            return subprocess.run(
                [
                    sys.executable,
                    str(VALIDATOR),
                    output_handle.name,
                    "--playlist",
                    playlist_handle.name,
                    "--catalog",
                    catalog_handle.name,
                    "--track",
                    str(track),
                ],
                capture_output=True,
                check=False,
                text=True,
            )

    def assert_rejected(
        self,
        text: str,
        message: str,
        spec: dict[str, object] | None = None,
    ) -> None:
        result = self.run_validator(text, spec)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(message, result.stdout)
        self.assertNotIn("Traceback", result.stderr)

    def test_golden_korean_track_reaches_plan_pass(self) -> None:
        result = self.run_validator(GOLDEN_OUTPUT)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PLAN PASS", result.stdout)
        self.assertIn("planned_duration=207.3s", result.stdout)
        self.assertIn("language=ko", result.stdout)
        self.assertIn("duration-ready", result.stdout)

    def test_playlist_mode_binds_output_to_selected_structure(self) -> None:
        catalog, playlist = valid_playlist_spec()
        spec = playlist["tracks"][0]["spec"]
        text = render_output(spec, bound_track_lyrics())
        result = self.run_playlist_validator(text, catalog, playlist)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("scope=playlist-track-1", result.stdout)

    def test_playlist_mode_rejects_trackspec_drift_from_slot(self) -> None:
        catalog, playlist = valid_playlist_spec()
        spec = playlist["tracks"][0]["spec"]
        spec["prompt_fields"]["Form/Flow"] = "Unbound replacement flow"
        text = render_output(spec, bound_track_lyrics())
        result = self.run_playlist_validator(text, catalog, playlist)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Form/Flow does not match selected slot", result.stdout)

    def test_golden_output_has_three_blocks_and_outside_title(self) -> None:
        self.assertEqual(GOLDEN_OUTPUT.count(FENCE + "text"), 3)
        self.assertEqual(GOLDEN_OUTPUT.count(FENCE), 6)
        before_lyrics = GOLDEN_OUTPUT.index("**가사**")
        title_position = GOLDEN_OUTPUT.index("### 빗소리의 여백")
        exclusion_position = GOLDEN_OUTPUT.index("**절대불가프롬프트**")
        self.assertLess(exclusion_position, title_position)
        self.assertLess(title_position, before_lyrics)
        self.assertNotIn("Title:", golden_lyrics())
        self.assertNotIn("제목:", golden_lyrics())

    def test_rejects_missing_or_extra_output_blocks(self) -> None:
        missing = GOLDEN_OUTPUT.replace("**절대불가프롬프트**", "**제외**", 1)
        self.assert_rejected(missing, "Expected exactly one **절대불가프롬프트**")
        extra = GOLDEN_OUTPUT + f"\n{FENCE}text\nextra\n{FENCE}\n"
        self.assert_rejected(extra, "Expected exactly three fenced text blocks")

    def test_rejects_title_inside_lyrics_or_wrong_outside_title(self) -> None:
        inside = GOLDEN_OUTPUT.replace(
            "[Intro]", "Title: 빗소리의 여백\n\n[Intro]", 1
        )
        self.assert_rejected(inside, "Lyrics block must not contain a title line")
        wrong = GOLDEN_OUTPUT.replace("### 빗소리의 여백", "### 다른 제목", 1)
        self.assert_rejected(wrong, "Outside title mismatch")

    def test_rejects_old_five_block_shape(self) -> None:
        old_shape = GOLDEN_OUTPUT.replace(
            "**기본프롬프트**", "**Main Prompt A**", 1
        ).replace("### 빗소리의 여백", "**Title And Lyrics**", 1)
        self.assert_rejected(old_shape, "required order")

    def test_rejects_prompt_over_800_characters(self) -> None:
        spec = copy.deepcopy(GOLDEN_SPEC)
        fields = spec["prompt_fields"]
        assert isinstance(fields, dict)
        fields["Production/Mix"] += " polished warm detail" * 4
        self.assert_rejected(render_output(spec), "maximum is 800", spec)

    def test_rejects_prompt_that_does_not_compile_from_spec(self) -> None:
        text = GOLDEN_OUTPUT.replace("warm neo-soul", "cold metal", 1)
        self.assert_rejected(
            text,
            "Basic Prompt does not match TrackSpec compilation",
        )

    def test_rejects_bracket_or_negative_command_in_basic_prompt(self) -> None:
        spec = copy.deepcopy(GOLDEN_SPEC)
        fields = spec["prompt_fields"]
        assert isinstance(fields, dict)
        fields["Feel"] = "Rainy reading [Chorus] without motion"
        result = self.run_validator(render_output(spec), spec)
        self.assertEqual(result.returncode, 1)
        self.assertIn("bracketed text", result.stdout)
        self.assertIn("negative command", result.stdout)

    def test_rejects_exclusion_mismatch_overflow_and_duplication(self) -> None:
        mismatch = GOLDEN_OUTPUT.replace("male lead, duet, rap", "banjo, opera", 1)
        self.assert_rejected(
            mismatch,
            "Absolute Exclusion Prompt does not match TrackSpec",
        )

        spec = copy.deepcopy(GOLDEN_SPEC)
        spec["exclusion_prompt"] = "x" * 101
        self.assert_rejected(render_output(spec), "maximum is 100", spec)

        spec = copy.deepcopy(GOLDEN_SPEC)
        spec["exclusion_prompt"] = "Rhodes lead"
        self.assert_rejected(
            render_output(spec),
            "duplicated in Basic Prompt",
            spec,
        )

    def test_rejects_bracketed_structure_tag_in_exclusion_prompt(self) -> None:
        spec = copy.deepcopy(GOLDEN_SPEC)
        spec["exclusion_prompt"] = "[Chorus], trap hats"
        self.assert_rejected(
            render_output(spec),
            "bracketed text reserved for Lyrics",
            spec,
        )

    def test_accepts_empty_absolute_exclusion_block(self) -> None:
        spec = copy.deepcopy(GOLDEN_SPEC)
        spec["exclusion_prompt"] = ""
        result = self.run_validator(render_output(spec), spec)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_rejects_malformed_or_drifting_trackspec(self) -> None:
        spec = copy.deepcopy(GOLDEN_SPEC)
        spec["variant_overrides"] = {}
        self.assert_rejected(render_output(spec), "unknown keys", spec)

        spec = copy.deepcopy(GOLDEN_SPEC)
        fields = spec["prompt_fields"]
        assert isinstance(fields, dict)
        spec["prompt_fields"] = dict(reversed(list(fields.items())))
        self.assert_rejected(
            render_output(spec),
            "eight fields in required order",
            spec,
        )

        spec = copy.deepcopy(GOLDEN_SPEC)
        spec["target_duration_seconds"] = "soon"
        self.assert_rejected(
            render_output(spec),
            "target_duration_seconds must be numeric",
            spec,
        )

    def test_enforces_three_to_four_minute_plan_boundaries(self) -> None:
        bars = sum(section["bars"] for section in GOLDEN_SPEC["sections"])
        for bpm in (76, 101):
            with self.subTest(pass_bpm=bpm):
                spec = copy.deepcopy(GOLDEN_SPEC)
                spec["bpm"] = bpm
                spec["target_duration_seconds"] = round(bars * 4 * 60 / bpm, 1)
                result = self.run_validator(render_output(spec), spec)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        for bpm in (75, 102):
            with self.subTest(fail_bpm=bpm):
                spec = copy.deepcopy(GOLDEN_SPEC)
                spec["bpm"] = bpm
                spec["target_duration_seconds"] = round(bars * 4 * 60 / bpm, 1)
                self.assert_rejected(
                    render_output(spec),
                    "planned duration must be between 180 and 240 seconds",
                    spec,
                )

    def test_rejects_target_and_bar_plan_disagreement(self) -> None:
        spec = copy.deepcopy(GOLDEN_SPEC)
        spec["target_duration_seconds"] = 220
        self.assert_rejected(
            render_output(spec),
            "differ by more than 2 seconds",
            spec,
        )

    def test_rejects_short_placeholder_or_repeat_shorthand_lyrics(self) -> None:
        short = re.sub(
            r"(?ms)^\[Verse\].*?^\[Outro\]",
            "[Verse]\n짧은 노래\n\n[Outro]",
            golden_lyrics(),
        )
        self.assert_rejected(render_output(GOLDEN_SPEC, short), "tag sequence mismatch")

        placeholder = golden_lyrics().replace(
            "유리창에 번진 도시가", "TODO", 1
        )
        self.assert_rejected(
            render_output(GOLDEN_SPEC, placeholder),
            "placeholder text",
        )

        repeat = golden_lyrics().replace(
            "빗소리의 여백을 따라", "빗소리의 여백을 따라 x2", 1
        )
        self.assert_rejected(
            render_output(GOLDEN_SPEC, repeat),
            "repeat shorthand",
        )

    def test_rejects_empty_vocal_or_lyric_in_instrumental_section(self) -> None:
        empty_vocal = golden_lyrics().replace(
            "[Verse]\n유리창에 번진 도시가\n책상 위로 천천히 내려와\n"
            "젖은 골목의 작은 숨결\n문장 사이에 조용히 앉아",
            "[Verse]",
            1,
        )
        self.assert_rejected(
            render_output(GOLDEN_SPEC, empty_vocal),
            "Vocal section 2 [Verse] contains no lyric text",
        )

        instrumental_text = golden_lyrics().replace(
            "[Intro]\n\n[Verse]", "[Intro]\n빗방울 소리\n\n[Verse]", 1
        )
        self.assert_rejected(
            render_output(GOLDEN_SPEC, instrumental_text),
            "Instrumental section 1 [Intro] must not contain lyric text",
        )

    def test_rejects_tag_or_language_mismatch(self) -> None:
        bad_tag = golden_lyrics().replace("[Pre-Chorus]", "[First Window]", 1)
        result = self.run_validator(render_output(GOLDEN_SPEC, bad_tag))
        self.assertEqual(result.returncode, 1)
        self.assertIn("Unsupported Lyrics tags", result.stdout)
        self.assertIn("tag sequence mismatch", result.stdout)

        spec = copy.deepcopy(GOLDEN_SPEC)
        spec["language"] = "en"
        self.assert_rejected(
            render_output(spec),
            "lyrics language does not match en",
            spec,
        )


if __name__ == "__main__":
    unittest.main()
