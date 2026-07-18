#!/usr/bin/env python3
"""Validate one paste-ready track output against a bound or standalone TrackSpec."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path
from typing import Any


SECTION_NAMES = ("기본프롬프트", "절대불가프롬프트", "가사")
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
SPEC_KEYS = {
    "title",
    "language",
    "target_duration_seconds",
    "bpm",
    "metrical_pulses_per_bar",
    "sections",
    "prompt_fields",
    "exclusion_prompt",
}
SECTION_KEYS = {"tag", "bars", "vocal"}
SUPPORTED_TAGS = {
    "Intro",
    "Verse",
    "Pre-Chorus",
    "Chorus",
    "Bridge",
    "Outro",
    "Hook",
    "Refrain",
    "Break",
    "Drop",
    "Coda",
}
FENCE = chr(96) * 3
NEGATIVE_COMMAND = re.compile(
    r"\b(?:no|not|without|avoid|avoids|avoiding|exclude|excludes|excluding|never)\b",
    re.IGNORECASE,
)
BRACKETED_TEXT = re.compile(r"\[[^\]\n]+\]")
REPEAT_SHORTHAND = re.compile(
    r"(?:\b[x×]\s*[2-9]\s*$|^\s*repeat(?:\s+.+)?$)",
    re.IGNORECASE,
)
PLACEHOLDER = re.compile(
    r"(?:\b(?:TBD|TODO|placeholder)\b|<[^>\n]+>|\[(?:insert|approved|continue)[^\]]*\])",
    re.IGNORECASE,
)
TITLE_LINE = re.compile(r"(?mi)^\s*(?:title|제목)\s*:")
LATIN_WORD = re.compile(r"[A-Za-z]+(?:['’-][A-Za-z]+)?")
HANGUL = re.compile(r"[\uac00-\ud7a3]")
KANA = re.compile(r"[\u3040-\u30ff]")
HAN = re.compile(r"[\u3400-\u9fff]")
RESPIRATION_TOKEN = re.compile(
    r"\b(?:breath(?:e[sd]?|ing|y|iness|less|es)?|"
    r"inhale(?:s|d|ing)?|exhale(?:s|d|ing)?|"
    r"gasp(?:s|ed|ing)?|sigh(?:s|ed|ing)?)\b|"
    r"(?:\b숨(?:을|이|만|도|과|의)?\b|숨소리|숨결|호흡|들숨|날숨|한숨|息遣い|吐息|呼吸)",
    re.IGNORECASE,
)
ARTIFACT_ADJACENT_VOCAL_CUE = re.compile(
    r"\bsmoky(?:-clear)?\b|\bwhisper(?:s|ed|ing|y)?\b|\baudible\s+rests?\b|"
    r"\b(?:airy|intimate|near-field)(?:\s+low)?\s+(?:vocal|voice|lead|delivery|singing|tone)\b|"
    r"\b(?:very\s+)?close(?:\s+low)?\s+(?:vocal|voice|lead|delivery|singing|tone)\b|"
    r"\bclose(?:-|\s*)mic(?:'d|ed)?(?:\s+(?:vocal|voice|lead|delivery|singing|tone))?\b",
    re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument(
        "--spec",
        type=Path,
        help="Standalone TrackSpec JSON for an explicit single-track request",
    )
    source.add_argument(
        "--playlist",
        type=Path,
        help="Canonical ten-track PlaylistSpec JSON",
    )
    parser.add_argument(
        "--catalog",
        type=Path,
        help="Versioned structure catalog required with --playlist",
    )
    parser.add_argument(
        "--track",
        type=int,
        help="Bound track number required with --playlist",
    )
    return parser.parse_args()


def output_pattern() -> re.Pattern[str]:
    fence = re.escape(FENCE)
    return re.compile(
        rf"\A[ \t\r\n]*"
        rf"\*\*기본프롬프트\*\*[ \t]*\r?\n"
        rf"{fence}text[ \t]*\r?\n(?P<main>.*?)\r?\n{fence}[ \t]*\r?\n+"
        rf"\*\*절대불가프롬프트\*\*[ \t]*\r?\n"
        rf"{fence}text[ \t]*\r?\n(?P<exclusion>.*?)\r?\n{fence}[ \t]*\r?\n+"
        rf"###[ \t]+(?P<title>[^\r\n]+?)[ \t]*\r?\n+"
        rf"\*\*가사\*\*[ \t]*\r?\n"
        rf"{fence}text[ \t]*\r?\n(?P<lyrics>.*?)\r?\n{fence}"
        rf"[ \t\r\n]*\Z",
        re.DOTALL,
    )


def parse_output(text: str, errors: list[str]) -> dict[str, str]:
    heading_counts = {
        name: len(re.findall(rf"(?m)^\*\*{re.escape(name)}\*\*[ \t]*$", text))
        for name in SECTION_NAMES
    }
    for name, count in heading_counts.items():
        if count != 1:
            errors.append(f"Expected exactly one **{name}** heading; found {count}")

    fenced_blocks = re.findall(
        rf"(?ms)^{re.escape(FENCE)}text[ \t]*\r?\n.*?^{re.escape(FENCE)}[ \t]*$",
        text,
    )
    if len(fenced_blocks) != 3:
        errors.append(f"Expected exactly three fenced text blocks; found {len(fenced_blocks)}")

    match = output_pattern().fullmatch(text)
    if match is None:
        errors.append(
            "Output must be exactly Basic Prompt, Absolute Exclusion Prompt, "
            "outside level-three title, and Lyrics in the required order"
        )
        return {"main": "", "exclusion": "", "title": "", "lyrics": ""}
    return {name: value.strip() for name, value in match.groupdict().items()}


def is_positive_number(value: Any) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
        and value > 0
    )


def load_spec(path: Path, errors: list[str]) -> dict[str, Any] | None:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"Cannot read TrackSpec: {exc}")
        return None
    if not isinstance(raw, dict):
        errors.append("TrackSpec must be a JSON object")
        return None
    return raw


def validate_spec(
    spec: dict[str, Any],
    errors: list[str],
) -> dict[str, Any]:
    missing_keys = sorted(SPEC_KEYS - set(spec))
    unknown_keys = sorted(set(spec) - SPEC_KEYS)
    if missing_keys:
        errors.append("TrackSpec is missing keys: " + ", ".join(missing_keys))
    if unknown_keys:
        errors.append("TrackSpec has unknown keys: " + ", ".join(unknown_keys))

    title = spec.get("title")
    if (
        not isinstance(title, str)
        or not title.strip()
        or title != title.strip()
        or "\n" in title
        or "\r" in title
    ):
        errors.append("TrackSpec title must be one non-empty trimmed line")
        title = ""

    language = spec.get("language")
    if language not in {"en", "ko", "ja"}:
        errors.append("TrackSpec language must be en, ko, or ja")
        language = "auto"

    bpm = spec.get("bpm")
    if not is_positive_number(bpm):
        errors.append("TrackSpec bpm must be positive")
        bpm = None

    pulses = spec.get("metrical_pulses_per_bar")
    if not is_positive_number(pulses):
        errors.append("TrackSpec metrical_pulses_per_bar must be positive")
        pulses = None

    target = spec.get("target_duration_seconds")
    if not is_positive_number(target):
        errors.append("TrackSpec target_duration_seconds must be numeric")
        target = None
    elif not 180 <= float(target) <= 240:
        errors.append("TrackSpec target duration must be between 180 and 240 seconds")

    sections = spec.get("sections")
    normalized_sections: list[dict[str, Any]] = []
    if not isinstance(sections, list) or not sections:
        errors.append("TrackSpec sections must be a non-empty list")
    else:
        for index, section in enumerate(sections, start=1):
            if not isinstance(section, dict):
                errors.append(f"TrackSpec section {index} must be an object")
                continue
            section_missing = sorted(SECTION_KEYS - set(section))
            section_unknown = sorted(set(section) - SECTION_KEYS)
            if section_missing:
                errors.append(
                    f"TrackSpec section {index} is missing keys: "
                    + ", ".join(section_missing)
                )
            if section_unknown:
                errors.append(
                    f"TrackSpec section {index} has unknown keys: "
                    + ", ".join(section_unknown)
                )
            tag = section.get("tag")
            bars = section.get("bars")
            vocal = section.get("vocal")
            if tag not in SUPPORTED_TAGS:
                errors.append(f"TrackSpec section {index} has unsupported tag {tag}")
            if not is_positive_number(bars):
                errors.append(f"TrackSpec section {index} bars must be positive")
            if not isinstance(vocal, bool):
                errors.append(f"TrackSpec section {index} vocal must be boolean")
            if (
                tag in SUPPORTED_TAGS
                and is_positive_number(bars)
                and isinstance(vocal, bool)
            ):
                normalized_sections.append(
                    {"tag": tag, "bars": float(bars), "vocal": vocal}
                )

    prompt_fields = spec.get("prompt_fields")
    normalized_fields: dict[str, str] = {}
    if not isinstance(prompt_fields, dict):
        errors.append("TrackSpec prompt_fields must be an object")
    else:
        if tuple(prompt_fields) != MAIN_FIELDS:
            errors.append(
                "TrackSpec prompt_fields must contain the eight fields in required order"
            )
        missing = [field for field in MAIN_FIELDS if field not in prompt_fields]
        unknown = [field for field in prompt_fields if field not in MAIN_FIELDS]
        if missing:
            errors.append("TrackSpec prompt_fields is missing fields: " + ", ".join(missing))
        if unknown:
            errors.append("TrackSpec prompt_fields has unknown fields: " + ", ".join(unknown))
        for field in MAIN_FIELDS:
            value = prompt_fields.get(field)
            if (
                not isinstance(value, str)
                or not value.strip()
                or value != value.strip()
                or "\n" in value
                or "\r" in value
            ):
                errors.append(
                    f"TrackSpec prompt field {field} must be one non-empty trimmed line"
                )
            else:
                normalized_fields[field] = value

    exclusion = spec.get("exclusion_prompt")
    if not isinstance(exclusion, str):
        errors.append("TrackSpec exclusion_prompt must be a string")
        exclusion = ""
    elif "\n" in exclusion or "\r" in exclusion or exclusion != exclusion.strip():
        errors.append("TrackSpec exclusion_prompt must be one trimmed line")

    planned: float | None = None
    if bpm is not None and pulses is not None and normalized_sections:
        planned = (
            sum(section["bars"] for section in normalized_sections)
            * float(pulses)
            * 60
            / float(bpm)
        )
        if not 180 <= planned <= 240:
            errors.append(
                "TrackSpec planned duration must be between 180 and 240 seconds; "
                f"found {planned:.1f}"
            )
        if target is not None and abs(planned - float(target)) > 2:
            errors.append(
                "TrackSpec target and bar-plan duration differ by more than 2 seconds"
            )

    return {
        "title": title,
        "language": language,
        "sections": normalized_sections,
        "prompt_fields": normalized_fields,
        "exclusion_prompt": exclusion,
        "planned_duration": planned,
    }


def compile_basic_prompt(fields: dict[str, str]) -> str:
    if set(fields) != set(MAIN_FIELDS):
        return ""
    return " ".join(f"{field}: {fields[field]}" for field in MAIN_FIELDS)


def lyric_sections(lyrics: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"(?m)^\[([^\]\n]+)\][ \t]*$", lyrics))
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(lyrics)
        sections.append((match.group(1), lyrics[match.end() : end].strip()))
    return sections


def lyric_lines(text: str) -> list[str]:
    return [
        line.strip()
        for line in text.splitlines()
        if line.strip() and not re.fullmatch(r"\[[^\]\n]+\]", line.strip())
    ]


def lyric_unit_count(text: str, language: str) -> int:
    if language == "ko":
        return len(HANGUL.findall(text)) + len(LATIN_WORD.findall(text))
    if language == "ja":
        return (
            len(KANA.findall(text))
            + len(HAN.findall(text))
            + len(LATIN_WORD.findall(text))
        )
    return len(LATIN_WORD.findall(text))


def language_matches(text: str, language: str) -> bool:
    latin = len(LATIN_WORD.findall(text))
    hangul = len(HANGUL.findall(text))
    kana = len(KANA.findall(text))
    han = len(HAN.findall(text))
    if language == "en":
        return latin >= 20 and hangul + kana < max(10, latin)
    if language == "ko":
        return hangul >= 20
    if language == "ja":
        return kana >= 10 and kana + han >= 20
    return True


def validate_basic_prompt(
    main: str,
    expected_fields: dict[str, str],
    errors: list[str],
) -> int:
    expected = compile_basic_prompt(expected_fields)
    if not main:
        errors.append("Basic Prompt is empty")
    elif expected and main != expected:
        errors.append("Basic Prompt does not match TrackSpec compilation")
    if len(main) > 900:
        errors.append(f"Basic Prompt is {len(main)} characters; maximum is 900")
    if BRACKETED_TEXT.search(main):
        errors.append("Basic Prompt contains bracketed text reserved for Lyrics")
    if NEGATIVE_COMMAND.search(main):
        errors.append(
            "Basic Prompt contains a negative command reserved for Absolute Exclusion Prompt"
        )
    return len(main)


def validate_exclusion(
    exclusion: str,
    expected: str,
    main: str,
    errors: list[str],
) -> int:
    if exclusion != expected:
        errors.append("Absolute Exclusion Prompt does not match TrackSpec")
    if len(exclusion) > 100:
        errors.append(
            f"Absolute Exclusion Prompt is {len(exclusion)} characters; maximum is 100"
        )
    if BRACKETED_TEXT.search(exclusion):
        errors.append(
            "Absolute Exclusion Prompt contains bracketed text reserved for Lyrics"
        )
    for trait in (item.strip() for item in exclusion.split(",")):
        if trait and len(trait) >= 4 and trait.casefold() in main.casefold():
            errors.append(
                f"Absolute exclusion is duplicated in Basic Prompt: {trait}"
            )
    return len(exclusion)


def validate_lyrics(
    lyrics: str,
    language: str,
    spec_sections: list[dict[str, Any]],
    errors: list[str],
) -> tuple[int, int]:
    if TITLE_LINE.search(lyrics):
        errors.append("Lyrics block must not contain a title line")

    all_brackets = re.findall(r"\[([^\]\n]+)\]", lyrics)
    line_tags = re.findall(r"(?m)^\[([^\]\n]+)\][ \t]*$", lyrics)
    if all_brackets != line_tags:
        errors.append("Every bracketed Lyrics instruction must be a standalone tag")
    unsupported = [tag for tag in line_tags if tag not in SUPPORTED_TAGS]
    if unsupported:
        errors.append("Unsupported Lyrics tags: " + ", ".join(unsupported))
    expected_tags = [section["tag"] for section in spec_sections]
    if line_tags != expected_tags:
        errors.append(
            "Lyrics tag sequence mismatch: expected "
            + ",".join(expected_tags)
            + " but found "
            + ",".join(line_tags)
        )

    sections = lyric_sections(lyrics)
    lines = lyric_lines(lyrics)
    if not lines:
        errors.append("Lyrics block contains no lyric text")
    for line in lines:
        if PLACEHOLDER.search(line):
            errors.append("Lyrics block contains placeholder text")
            break
        if REPEAT_SHORTHAND.search(line):
            errors.append("Lyrics block contains repeat shorthand; write every return")
            break

    if spec_sections and len(sections) == len(spec_sections):
        for index, ((tag, content), planned_section) in enumerate(
            zip(sections, spec_sections, strict=True),
            start=1,
        ):
            content_lines = lyric_lines(content)
            if planned_section["vocal"] and not content_lines:
                errors.append(f"Vocal section {index} [{tag}] contains no lyric text")
            if not planned_section["vocal"] and content_lines:
                errors.append(
                    f"Instrumental section {index} [{tag}] must not contain lyric text"
                )

    measurement_text = "\n".join(lines)
    units = lyric_unit_count(measurement_text, language)
    if lines and not language_matches(measurement_text, language):
        errors.append(f"lyrics language does not match {language}")

    if spec_sections and len(sections) == len(spec_sections):
        vocal_pairs = [
            (content, planned_section)
            for (_, content), planned_section in zip(
                sections, spec_sections, strict=True
            )
            if planned_section["vocal"]
        ]
        vocal_text = "\n".join(content for content, _ in vocal_pairs)
        vocal_line_count = len(lyric_lines(vocal_text))
        vocal_bars = sum(section["bars"] for _, section in vocal_pairs)
        measured_units = lyric_unit_count(vocal_text, language)
        minimum_lines = max(12, math.ceil(vocal_bars / 3))
        unit_factor = 2 if language == "en" else 3
        minimum_units = max(80, math.ceil(vocal_bars * unit_factor))
        maximum_units = math.ceil(vocal_bars * 12)
        if vocal_line_count < minimum_lines or measured_units < minimum_units:
            errors.append(
                "Lyrics are too short for a 3-4 minute target: "
                f"{vocal_line_count} lines/{measured_units} units; "
                f"need at least {minimum_lines} lines/{minimum_units} units"
            )
        if measured_units > maximum_units:
            errors.append(
                "Lyrics are too dense for a 3-4 minute target: "
                f"{measured_units} units; maximum readiness bound is {maximum_units}"
            )

    return len(lines), units


def validate(
    text: str,
    spec: dict[str, Any] | None,
) -> tuple[list[str], dict[str, float | int | str]]:
    errors: list[str] = []
    compiled = parse_output(text, errors)
    normalized_spec = validate_spec(spec, errors) if spec is not None else {
        "title": "",
        "language": "auto",
        "sections": [],
        "prompt_fields": {},
        "exclusion_prompt": "",
        "planned_duration": None,
    }

    for label, value in (
        ("Basic Prompt", compiled["main"]),
        ("Absolute Exclusion Prompt", compiled["exclusion"]),
        ("Title", compiled["title"]),
        ("Lyrics", compiled["lyrics"]),
    ):
        match = RESPIRATION_TOKEN.search(value)
        if match:
            errors.append(
                f"Active generation payload contains respiration-related token in {label}: "
                f"{match.group(0)}"
            )
        adjacent_match = ARTIFACT_ADJACENT_VOCAL_CUE.search(value)
        if adjacent_match:
            errors.append(
                f"Active generation payload contains artifact-linked vocal cue in {label}: "
                f"{adjacent_match.group(0)}"
            )

    main_length = validate_basic_prompt(
        compiled["main"], normalized_spec["prompt_fields"], errors
    )
    exclusion_length = validate_exclusion(
        compiled["exclusion"],
        normalized_spec["exclusion_prompt"],
        compiled["main"],
        errors,
    )

    if compiled["title"] != normalized_spec["title"]:
        errors.append(
            f"Outside title mismatch: expected {normalized_spec['title']!r} "
            f"but found {compiled['title']!r}"
        )

    lyric_line_count, lyric_units = validate_lyrics(
        compiled["lyrics"],
        normalized_spec["language"],
        normalized_spec["sections"],
        errors,
    )

    return errors, {
        "planned_duration": normalized_spec["planned_duration"] or 0,
        "language": normalized_spec["language"],
        "lyric_lines": lyric_line_count,
        "lyric_units": lyric_units,
        "Basic": main_length,
        "Exclusion": exclusion_length,
    }


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    try:
        text = args.output.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"ERROR: Cannot read output: {exc}")
        return 1

    validation_scope = "single-track"
    spec: dict[str, Any] | None = None
    if args.playlist is not None:
        if args.catalog is None or args.track is None:
            print("ERROR: --playlist requires both --catalog and --track")
            return 1
        from validate_playlist_spec import load_and_validate

        playlist_errors, tracks = load_and_validate(args.playlist, args.catalog)
        errors.extend(playlist_errors)
        bound_track = tracks.get(args.track)
        if bound_track is None:
            errors.append(f"PlaylistSpec has no bound track {args.track}")
        else:
            bound_spec = bound_track.get("spec")
            if isinstance(bound_spec, dict):
                spec = bound_spec
            else:
                errors.append(f"Bound track {args.track} has no valid TrackSpec")
        validation_scope = f"playlist-track-{args.track}"
    else:
        if args.catalog is not None or args.track is not None:
            print("ERROR: --catalog and --track are valid only with --playlist")
            return 1
        spec = load_spec(args.spec, errors)

    validation_errors, measurements = validate(text, spec)
    errors.extend(validation_errors)
    if errors:
        for error in dict.fromkeys(errors):
            print(f"ERROR: {error}")
        return 1

    print(
        "PLAN PASS: "
        f"scope={validation_scope}, "
        f"planned_duration={measurements['planned_duration']:.1f}s, "
        f"language={measurements['language']}, "
        f"lyric_lines={measurements['lyric_lines']}, "
        f"lyric_units={measurements['lyric_units']}, "
        f"Basic={measurements['Basic']}, "
        f"Exclusion={measurements['Exclusion']}, duration-ready"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
