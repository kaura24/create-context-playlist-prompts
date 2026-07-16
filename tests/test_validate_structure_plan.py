from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_structure_plan.py"


def valid_plan() -> dict[str, object]:
    profiles = (
        ("central", "verse-refrain", "V1", "E1"),
        ("central", "chorus-led", "V2", "E2"),
        ("adjacent", "through-composed", "V3", "E3"),
    )
    candidates: list[dict[str, object]] = []
    for number in range(1, 51):
        genre_lane, form_id, envelope_id, evidence_id = profiles[(number - 1) % 3]
        optional_sections = ("Verse", "Pre-Chorus", "Chorus", "Bridge", "Break", "Refrain")
        section_sequence = ["Intro"] + [
            section
            for bit, section in enumerate(optional_sections)
            if number & (1 << bit)
        ] + ["Outro"]
        candidates.append(
            {
                "candidate_id": f"C{number:03d}",
                "genre_lane": genre_lane,
                "form_id": form_id,
                "envelope_id": envelope_id,
                "evidence_ids": [evidence_id],
                "section_sequence": section_sequence,
                "recurrence": f"recurrence-{number}",
                "entry": f"entry-{(number - 1) % 5 + 1}",
                "contrast_peak": f"contrast-peak-{(number - 1) % 5 + 1}",
                "transition_interlude": f"transition-{(number - 1) % 5 + 1}",
                "ending": f"ending-{(number - 1) % 5 + 1}",
                "hook_return": "Repeated hook" if number % 2 else "Varied return",
            }
        )

    plan: dict[str, object] = {
        "genre_coordinate": "Korean 2020s indie neo-soul, slow pocket",
        "evidence": [
            {"id": "E1", "source": "source-1", "scope": "central form and entry"},
            {"id": "E2", "source": "source-2", "scope": "central contrast and peak"},
            {"id": "E3", "source": "source-3", "scope": "adjacent ending and return"},
        ],
        "genre_lanes": [
            {"id": "central", "label": "central neo-soul", "evidence_ids": ["E1", "E2"]},
            {"id": "adjacent", "label": "approved adjacent art-soul", "evidence_ids": ["E3"]},
        ],
        "variation_envelopes": [
            {"id": "V1", "genre_lane": "central", "form_id": "verse-refrain", "evidence_ids": ["E1"]},
            {"id": "V2", "genre_lane": "central", "form_id": "chorus-led", "evidence_ids": ["E2"]},
            {"id": "V3", "genre_lane": "adjacent", "form_id": "through-composed", "evidence_ids": ["E3"]},
        ],
        "candidate_pool": {
            "minimum_count": 50,
            "dimension_requirements": {
                "genre_lane": 2,
                "form_id": 3,
                "section_sequence": 50,
                "recurrence": 50,
                "entry": 5,
                "contrast_peak": 5,
                "transition_interlude": 5,
                "ending": 5,
                "hook_return": 2,
            },
            "candidates": candidates,
        },
        "selection_contract": {
            "track_count": 10,
            "envelope_allocations": [
                {"envelope_id": "V1", "track_count": 4},
                {"envelope_id": "V2", "track_count": 3},
                {"envelope_id": "V3", "track_count": 3},
            ],
            "dimension_requirements": {
                "genre_lane": 2,
                "form_id": 3,
                "section_sequence": 10,
                "recurrence": 10,
                "entry": 5,
                "contrast_peak": 5,
                "transition_interlude": 5,
                "ending": 5,
                "hook_return": 2,
            },
        },
        "selections": [
            {
                "track": number,
                "slot_id": f"S{number:02d}",
                "candidate_id": f"C{number:03d}",
                "locked_fingerprint": {
                    key: value
                    for key, value in candidates[number - 1].items()
                    if key
                    in {
                        "genre_lane",
                        "form_id",
                        "section_sequence",
                        "recurrence",
                        "entry",
                        "contrast_peak",
                        "transition_interlude",
                        "ending",
                        "hook_return",
                    }
                },
                "open_axes": ["section density curve"],
                "state": "reserved",
            }
            for number in range(1, 11)
        ],
    }
    envelopes = plan["variation_envelopes"]
    assert isinstance(envelopes, list)
    for envelope in envelopes:
        assert isinstance(envelope, dict)
        envelope["permitted_combinations"] = [
            {
                key: value
                for key, value in candidate.items()
                if key
                in {
                    "genre_lane",
                    "form_id",
                    "section_sequence",
                    "recurrence",
                    "entry",
                    "contrast_peak",
                    "transition_interlude",
                    "ending",
                    "hook_return",
                }
            }
            for candidate in candidates
            if candidate["envelope_id"] == envelope["id"]
        ]
        envelope["forbidden_combinations"] = []
    return plan


class StructurePlanValidatorTests(unittest.TestCase):
    def run_validator(self, plan: dict[str, object]) -> subprocess.CompletedProcess[str]:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json") as handle:
            json.dump(plan, handle)
            handle.flush()
            return subprocess.run(
                [sys.executable, str(VALIDATOR), handle.name],
                capture_output=True,
                check=False,
                text=True,
            )

    def test_accepts_fifty_candidate_genre_plan_and_ten_slots(self) -> None:
        result = self.run_validator(valid_plan())
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS: 50 genre-valid candidates; 10 structural slots", result.stdout)

    def test_rejects_candidate_pool_below_fifty(self) -> None:
        plan = valid_plan()
        pool = plan["candidate_pool"]
        assert isinstance(pool, dict)
        candidates = pool["candidates"]
        assert isinstance(candidates, list)
        pool["candidates"] = candidates[:49]
        result = self.run_validator(plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("at least 50 candidates", result.stdout)

    def test_rejects_duplicate_candidate_fingerprint(self) -> None:
        plan = valid_plan()
        pool = plan["candidate_pool"]
        assert isinstance(pool, dict)
        candidates = pool["candidates"]
        assert isinstance(candidates, list)
        duplicate = deepcopy(candidates[0])
        duplicate["candidate_id"] = "C002"
        candidates[1] = duplicate
        result = self.run_validator(plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("duplicate structural fingerprint", result.stdout)

    def test_rejects_selection_allocation_mismatch(self) -> None:
        plan = valid_plan()
        selections = plan["selections"]
        assert isinstance(selections, list)
        selections[0]["candidate_id"] = "C002"
        result = self.run_validator(plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("envelope allocation", result.stdout)

    def test_rejects_unmet_selection_dimension_requirement(self) -> None:
        plan = valid_plan()
        contract = plan["selection_contract"]
        assert isinstance(contract, dict)
        requirements = contract["dimension_requirements"]
        assert isinstance(requirements, dict)
        requirements["entry"] = 6
        result = self.run_validator(plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("entry requires 6 distinct values", result.stdout)

    def test_rejects_unregistered_evidence(self) -> None:
        plan = valid_plan()
        pool = plan["candidate_pool"]
        assert isinstance(pool, dict)
        candidates = pool["candidates"]
        assert isinstance(candidates, list)
        candidates[0]["evidence_ids"] = ["UNKNOWN"]
        result = self.run_validator(plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("unknown evidence id UNKNOWN", result.stdout)

    def test_rejects_unsupported_suno_section_name(self) -> None:
        plan = valid_plan()
        pool = plan["candidate_pool"]
        assert isinstance(pool, dict)
        candidates = pool["candidates"]
        assert isinstance(candidates, list)
        candidates[0]["section_sequence"] = ["Cold Open", "Verse", "Chorus"]
        result = self.run_validator(plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("unsupported Suno section Cold Open", result.stdout)

    def test_rejects_description_that_references_absent_section(self) -> None:
        plan = valid_plan()
        pool = plan["candidate_pool"]
        assert isinstance(pool, dict)
        candidates = pool["candidates"]
        assert isinstance(candidates, list)
        candidates[0]["transition_interlude"] = "Bridge opens into Chorus"
        result = self.run_validator(plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("mentions absent section Bridge", result.stdout)

    def test_rejects_candidate_outside_permitted_complete_combination(self) -> None:
        plan = valid_plan()
        pool = plan["candidate_pool"]
        assert isinstance(pool, dict)
        candidates = pool["candidates"]
        assert isinstance(candidates, list)
        candidates[0]["section_sequence"] = ["Drop", "Coda"]
        result = self.run_validator(plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("not a permitted complete combination", result.stdout)

    def test_accepts_lifecycle_states_after_full_design(self) -> None:
        plan = valid_plan()
        selections = plan["selections"]
        assert isinstance(selections, list)
        selections[0]["state"] = "active"
        selections[0]["main_prompt_form_flow"] = "instrumental introduction, repeated refrain arc, bridge contrast, final release"
        selections[1]["state"] = "finalized"
        selections[1]["main_prompt_form_flow"] = "chorus-led opening, verse development, final close"
        result = self.run_validator(plan)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_rejects_selection_with_wrong_locked_fingerprint(self) -> None:
        plan = valid_plan()
        selections = plan["selections"]
        assert isinstance(selections, list)
        fingerprint = selections[0]["locked_fingerprint"]
        assert isinstance(fingerprint, dict)
        fingerprint["ending"] = "wrong ending"
        result = self.run_validator(plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("locked_fingerprint does not match", result.stdout)


if __name__ == "__main__":
    unittest.main()
