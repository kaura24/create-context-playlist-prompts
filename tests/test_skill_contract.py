from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
REFERENCES = ROOT / "references"
PLAYLIST_FIXTURE = ROOT / "tests" / "fixtures" / "playlist-map-ko.md"


class SkillContractTests(unittest.TestCase):
    def operational_markdown(self) -> str:
        paths = [SKILL, *sorted(REFERENCES.glob("*.md"))]
        return "\n".join(path.read_text(encoding="utf-8") for path in paths)

    def test_workflow_declares_autonomy_and_one_checkpoint(self) -> None:
        text = self.operational_markdown()
        self.assertIn("Autonomy Contract", text)
        self.assertIn("single design checkpoint", text.lower())
        self.assertIn("reversible assumption", text.lower())

    def test_serial_blocker_phrases_are_removed(self) -> None:
        text = self.operational_markdown().lower()
        blocked_phrases = (
            "approve these artifacts sequentially",
            "blocks dependent work",
            "stop before reference approval",
            "do not proceed to the 10-track design",
            "get user approval for the genre-level",
        )
        for phrase in blocked_phrases:
            self.assertNotIn(phrase, text)

    def test_three_to_four_minute_lyrics_contract_is_explicit(self) -> None:
        text = self.operational_markdown().lower()
        self.assertIn("3-4 minute", text)
        self.assertIn("180-240 seconds", text)
        self.assertIn("duration readiness", text)

    def test_final_output_contract_is_three_blocks_with_outside_title(self) -> None:
        text = (REFERENCES / "output-contract.md").read_text(encoding="utf-8")
        for heading in ("**기본프롬프트**", "**절대불가프롬프트**", "**가사**"):
            self.assertIn(heading, text)
        self.assertIn("exactly three fenced blocks", text)
        self.assertIn("title only in the level-three heading", text)
        self.assertIn("Never put a title line inside a code block", text)

    def test_default_contract_has_one_prompt_source_of_truth(self) -> None:
        text = self.operational_markdown()
        self.assertIn("prompt_fields", text)
        self.assertNotIn("variant_overrides", text)
        self.assertNotIn("Main Prompt A", text)
        self.assertNotIn("A/B/C", text)

    def test_skill_uses_progressive_disclosure_and_valid_links(self) -> None:
        skill_text = SKILL.read_text(encoding="utf-8")
        self.assertLessEqual(len(skill_text.splitlines()), 160)
        links = re.findall(r"\[[^\]]+\]\((references/[^)]+\.md)\)", skill_text)
        self.assertTrue(links)
        for link in links:
            self.assertTrue((ROOT / link).is_file(), link)

    def test_operational_contract_stays_compact(self) -> None:
        text = self.operational_markdown()
        self.assertLessEqual(len(text.splitlines()), 600)
        self.assertLessEqual(len(re.findall(r"\bask\b", text, re.IGNORECASE)), 3)

    def test_evidence_labels_are_defined(self) -> None:
        text = (REFERENCES / "quality-and-render-protocol.md").read_text(
            encoding="utf-8"
        )
        for label in (
            "planned",
            "PLAN PASS",
            "draft-validated",
            "render-duration-verified",
            "render-verified",
        ):
            self.assertIn(f"| {label} |", text)

    def test_process_only_documents_are_not_in_skill_package(self) -> None:
        self.assertFalse((ROOT / "HANDOVER.md").exists())
        self.assertFalse((ROOT / "README.md").exists())

    def test_integration_fixture_contains_exactly_ten_duration_ready_rows(self) -> None:
        text = PLAYLIST_FIXTURE.read_text(encoding="utf-8")
        rows = re.findall(r"(?m)^\|\s*(\d+)\s*\|.*?\b(\d+)초\s*\|", text)
        self.assertEqual([int(number) for number, _ in rows], list(range(1, 11)))
        for _, seconds in rows:
            self.assertGreaterEqual(int(seconds), 180)
            self.assertLessEqual(int(seconds), 240)


if __name__ == "__main__":
    unittest.main()
