#!/usr/bin/env python3
"""Validate the deterministic parts of one compiled track output."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SECTION_NAMES = (
    "Main Prompt A",
    "Main Prompt B",
    "Main Prompt C",
    "Exclusion Prompt",
    "Title And Lyrics",
)
MAIN_FIELDS = (
    "Style:",
    "Feel:",
    "Tempo/Groove:",
    "Vocal:",
    "Instrumentation:",
    "Harmony:",
    "Form/Flow:",
    "Production/Mix:",
)
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
NEGATIVE_COMMAND = re.compile(
    r"\b(?:no|not|without|avoid|avoids|avoiding|exclude|excludes|excluding|never)\b",
    re.IGNORECASE,
)
IDENTICAL_WORDING = re.compile(r"\b(?:same|identical)\b|동일", re.IGNORECASE)
BRACKETED_TEXT = re.compile(r"\[[^\]\n]+\]")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--expected-tags",
        help="Comma-separated Lyrics tag sequence, for example Intro,Verse,Chorus,Outro",
    )
    return parser.parse_args()


def extract_section(text: str, name: str, errors: list[str]) -> tuple[int, str]:
    header = re.compile(rf"(?m)^\*\*{re.escape(name)}\*\*\s*$")
    matches = list(header.finditer(text))
    if len(matches) != 1:
        errors.append(f"Expected exactly one **{name}** heading; found {len(matches)}")
        return -1, ""

    match = matches[0]
    remainder = text[match.end() :]
    block = re.match(r"\s*```text[ \t]*\n(.*?)\n```", remainder, re.DOTALL)
    if not block:
        errors.append(f"**{name}** must be followed by one fenced text block")
        return match.start(), ""
    return match.start(), block.group(1).strip()


def validate(text: str, expected_tags: list[str] | None) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    sections: dict[str, str] = {}
    positions: list[int] = []

    for name in SECTION_NAMES:
        position, content = extract_section(text, name, errors)
        positions.append(position)
        sections[name] = content

    if all(position >= 0 for position in positions) and positions != sorted(positions):
        errors.append("Output sections are not in the required A, B, C, Exclusion, Lyrics order")

    fenced_blocks = re.findall(r"(?ms)^```text[ \t]*\n.*?^```[ \t]*$", text)
    if len(fenced_blocks) != 5:
        errors.append(f"Expected exactly five fenced text blocks; found {len(fenced_blocks)}")

    comparison_end = positions[0] if positions and positions[0] >= 0 else 0
    if IDENTICAL_WORDING.search(text[:comparison_end]):
        errors.append("Comparison table labels musical fields as same or identical; use fixed/shared scaffold wording")

    lengths: dict[str, int] = {}
    main_contents: list[str] = []
    for label in ("A", "B", "C"):
        name = f"Main Prompt {label}"
        content = sections[name]
        lengths[label] = len(content)
        main_contents.append(content)
        if not content:
            continue
        if len(content) > 800:
            errors.append(f"{name} is {len(content)} characters; maximum is 800")
        for field in MAIN_FIELDS:
            if field not in content:
                errors.append(f"{name} is missing required field {field}")
        if BRACKETED_TEXT.search(content):
            errors.append(f"{name} contains bracketed text")
        if NEGATIVE_COMMAND.search(content):
            errors.append(f"{name} contains a negative command reserved for Exclusion Prompt")
        if IDENTICAL_WORDING.search(content):
            errors.append(f"{name} describes eligible musical content as same or identical")

    if len(set(main_contents)) != 3:
        errors.append("Main Prompts A, B, and C must be three distinct controlled alternatives")

    exclusion = sections["Exclusion Prompt"]
    lengths["Exclusion"] = len(exclusion)
    if len(exclusion) > 100:
        errors.append(f"Exclusion Prompt is {len(exclusion)} characters; maximum is 100")

    lyrics = sections["Title And Lyrics"]
    title_lines = re.findall(r"(?m)^Title:\s+\S.*$", lyrics)
    if len(title_lines) != 1:
        errors.append(f"Title And Lyrics must contain exactly one Title line; found {len(title_lines)}")

    all_brackets = re.findall(r"\[([^\]\n]+)\]", lyrics)
    line_tags = re.findall(r"(?m)^\[([^\]\n]+)\]\s*$", lyrics)
    if all_brackets != line_tags:
        errors.append("Every bracketed Lyrics instruction must be a standalone supported structural tag")
    unsupported = [tag for tag in line_tags if tag not in SUPPORTED_TAGS]
    if unsupported:
        errors.append(f"Unsupported Lyrics tags: {', '.join(unsupported)}")
    if not line_tags:
        errors.append("Title And Lyrics contains no supported structural tags")
    if expected_tags is not None and line_tags != expected_tags:
        errors.append(
            "Lyrics tag sequence mismatch: expected "
            + ",".join(expected_tags)
            + " but found "
            + ",".join(line_tags)
        )

    return errors, lengths


def main() -> int:
    args = parse_args()
    expected_tags = args.expected_tags.split(",") if args.expected_tags else None
    text = args.output.read_text(encoding="utf-8")
    errors, lengths = validate(text, expected_tags)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(
        "PASS: "
        + ", ".join(f"{name}={length}" for name, length in lengths.items())
        + " characters"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
