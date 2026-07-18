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
FINGERPRINT_FIELDS = (
    "genre_lane",
    "form_id",
    "section_sequence",
    "recurrence",
    "entry",
    "contrast_peak",
    "transition_interlude",
    "ending",
    "hook_return",
)


def project(candidate: dict[str, object]) -> dict[str, object]:
    return {field: candidate[field] for field in FINGERPRINT_FIELDS}


def valid_catalog_and_plan() -> tuple[dict[str, object], dict[str, object]]:
    profiles = (
        ("central", "verse-refrain", "V1", "E1"),
        ("central", "chorus-led", "V2", "E2"),
        ("adjacent", "through-composed", "V3", "E3"),
    )
    candidates: list[dict[str, object]] = []
    for number in range(1, 51):
        genre_lane, form_id, envelope_id, evidence_id = profiles[(number - 1) % 3]
        optional_sections = (
            "Verse",
            "Pre-Chorus",
            "Chorus",
            "Bridge",
            "Break",
            "Refrain",
        )
        sequence = ["Intro"] + [
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
                "section_sequence": sequence,
                "recurrence": f"return-pattern-{number:02d}",
                "entry": f"entry-{(number - 1) % 5 + 1}",
                "contrast_peak": f"peak-{(number - 1) % 7 + 1}",
                "transition_interlude": f"transition-{(number - 1) % 4 + 1}",
                "ending": f"ending-{(number - 1) % 6 + 1}",
                "hook_return": "Repeated hook" if number % 2 else "Varied return",
            }
        )

    envelopes: list[dict[str, object]] = []
    for envelope_id, lane, form_id, evidence_id in (
        ("V1", "central", "verse-refrain", "E1"),
        ("V2", "central", "chorus-led", "E2"),
        ("V3", "adjacent", "through-composed", "E3"),
    ):
        envelopes.append(
            {
                "id": envelope_id,
                "genre_lane": lane,
                "form_id": form_id,
                "evidence_ids": [evidence_id],
                "permitted_combinations": [
                    project(candidate)
                    for candidate in candidates
                    if candidate["envelope_id"] == envelope_id
                ],
                "forbidden_combinations": [],
            }
        )

    catalog: dict[str, object] = {
        "catalog_revision": "test-catalog-v1",
        "genre_coordinate": "Korean 2020s indie neo-soul, slow pocket",
        "evidence": [
            {
                "id": "E1",
                "source": "https://example.com/form-entry",
                "scope": "central form and entry",
            },
            {
                "id": "E2",
                "source": "https://example.com/contrast-peak",
                "scope": "central contrast and peak",
            },
            {
                "id": "E3",
                "source": "https://example.com/adjacent-pattern",
                "scope": "adjacent ending and return",
            },
        ],
        "genre_lanes": [
            {
                "id": "central",
                "label": "central neo-soul",
                "evidence_ids": ["E1", "E2"],
            },
            {
                "id": "adjacent",
                "label": "approved adjacent art-soul",
                "evidence_ids": ["E3"],
            },
        ],
        "variation_envelopes": envelopes,
        "diversity_contract": {
            "candidate_minimums": {
                "genre_lane": 2,
                "form_id": 3,
                "section_sequence": 50,
                "recurrence": 50,
                "entry": 5,
                "contrast_peak": 7,
                "transition_interlude": 4,
                "ending": 6,
                "hook_return": 2,
            },
            "selection_minimums": {
                "genre_lane": 2,
                "form_id": 3,
                "section_sequence": 10,
                "recurrence": 10,
                "entry": 5,
                "contrast_peak": 7,
                "transition_interlude": 4,
                "ending": 6,
                "hook_return": 2,
            },
            "minimum_candidate_distance": 3,
            "minimum_selection_distance": 3,
        },
    }

    selections = []
    for number in range(1, 11):
        candidate = candidates[number - 1]
        selections.append(
            {
                "track": number,
                "slot_id": f"S{number:02d}",
                "candidate_id": candidate["candidate_id"],
                "reference_evidence_id": candidate["evidence_ids"][0],
                "locked_fingerprint": project(candidate),
                "open_axes": ["section density curve"],
                "state": "reserved",
            }
        )

    plan: dict[str, object] = {
        "catalog_revision": "test-catalog-v1",
        "candidate_pool": {
            "minimum_count": 50,
            "candidates": candidates,
        },
        "selection_contract": {
            "track_count": 10,
            "envelope_allocations": [
                {"envelope_id": "V1", "track_count": 4},
                {"envelope_id": "V2", "track_count": 3},
                {"envelope_id": "V3", "track_count": 3},
            ],
        },
        "selections": selections,
    }
    return catalog, plan


class StructurePlanValidatorTests(unittest.TestCase):
    def run_validator(
        self,
        catalog: dict[str, object],
        plan: dict[str, object],
    ) -> subprocess.CompletedProcess[str]:
        with (
            tempfile.NamedTemporaryFile(
                "w", encoding="utf-8", suffix=".json"
            ) as plan_handle,
            tempfile.NamedTemporaryFile(
                "w", encoding="utf-8", suffix=".json"
            ) as catalog_handle,
        ):
            json.dump(plan, plan_handle)
            plan_handle.flush()
            json.dump(catalog, catalog_handle)
            catalog_handle.flush()
            return subprocess.run(
                [
                    sys.executable,
                    str(VALIDATOR),
                    plan_handle.name,
                    "--catalog",
                    catalog_handle.name,
                ],
                capture_output=True,
                check=False,
                text=True,
            )

    def test_accepts_catalog_bound_fifty_candidate_plan(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("50 catalog-bound candidates; 10 structural slots", result.stdout)

    def test_rejects_catalog_revision_mismatch(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        plan["catalog_revision"] = "wrong-revision"
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("catalog_revision does not match", result.stdout)

    def test_rejects_evidence_without_url_or_user_approval(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        evidence = catalog["evidence"]
        assert isinstance(evidence, list)
        evidence[0]["source"] = "source-1"
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("must be an http(s) URL or user: approval", result.stdout)

    def test_selected_slots_require_candidate_cited_web_references(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        plan["selections"][0].pop("reference_evidence_id")
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("reference_evidence_id must be non-empty", result.stdout)

        catalog, plan = valid_catalog_and_plan()
        catalog["evidence"][0]["source"] = "user:approved-reference"
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("must resolve to an HTTP(S) source", result.stdout)

        catalog, plan = valid_catalog_and_plan()
        plan["selections"][0]["reference_evidence_id"] = "E2"
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("is not cited by candidate", result.stdout)

    def test_rejects_candidate_pool_below_fifty(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        pool = plan["candidate_pool"]
        assert isinstance(pool, dict)
        candidates = pool["candidates"]
        assert isinstance(candidates, list)
        pool["candidates"] = candidates[:49]
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("at least 50 candidates", result.stdout)

    def test_rejects_superficial_recurrence_only_candidates(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        pool = plan["candidate_pool"]
        assert isinstance(pool, dict)
        candidates = pool["candidates"]
        assert isinstance(candidates, list)
        for candidate in candidates:
            candidate.update(
                section_sequence=["Intro", "Verse", "Chorus", "Outro"],
                entry="same-entry",
                contrast_peak="same-peak",
                transition_interlude="same-transition",
                ending="same-ending",
                hook_return="Repeated hook",
            )
        envelopes = catalog["variation_envelopes"]
        assert isinstance(envelopes, list)
        for envelope in envelopes:
            envelope["permitted_combinations"] = [
                project(candidate)
                for candidate in candidates
                if candidate["envelope_id"] == envelope["id"]
            ]
        selections = plan["selections"]
        assert isinstance(selections, list)
        by_id = {candidate["candidate_id"]: candidate for candidate in candidates}
        for selection in selections:
            selection["locked_fingerprint"] = project(
                by_id[selection["candidate_id"]]
            )
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("structural distance", result.stdout)

    def test_catalog_owns_dimension_minimums(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        contract = catalog["diversity_contract"]
        assert isinstance(contract, dict)
        minimums = contract["selection_minimums"]
        assert isinstance(minimums, dict)
        minimums["entry"] = 6
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("entry requires 6 distinct values", result.stdout)

    def test_rejects_duplicate_candidate_fingerprint(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        pool = plan["candidate_pool"]
        assert isinstance(pool, dict)
        candidates = pool["candidates"]
        assert isinstance(candidates, list)
        duplicate = deepcopy(candidates[0])
        duplicate["candidate_id"] = "C002"
        candidates[1] = duplicate
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("duplicate structural fingerprint", result.stdout)

    def test_rejects_candidate_outside_catalog_envelope(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        pool = plan["candidate_pool"]
        assert isinstance(pool, dict)
        candidates = pool["candidates"]
        assert isinstance(candidates, list)
        candidates[0]["section_sequence"] = ["Drop", "Coda"]
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("not a permitted complete combination", result.stdout)

    def test_rejects_selection_with_wrong_locked_fingerprint(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        selections = plan["selections"]
        assert isinstance(selections, list)
        fingerprint = selections[0]["locked_fingerprint"]
        assert isinstance(fingerprint, dict)
        fingerprint["ending"] = "wrong-ending"
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("locked_fingerprint does not match", result.stdout)

    def test_accepts_post_design_lifecycle_snapshot(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        selections = plan["selections"]
        assert isinstance(selections, list)
        selections[0]["state"] = "active"
        selections[0]["main_prompt_form_flow"] = "approved active flow"
        selections[1]["state"] = "finalized"
        selections[1]["main_prompt_form_flow"] = "approved finalized flow"
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
