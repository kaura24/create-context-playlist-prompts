from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_lyric_review.py"
LYRICS = """[Verse]
I left the office just past two
Your message waited on my phone

[Chorus]
The light turns green and I drive home"""
OUTPUT = f"""**기본프롬프트**
```text
Style: Test
```

**절대불가프롬프트**
```text

```

### Test

**가사**
```text
{LYRICS}
```
"""
CRITERIA = (
    "design_traceability",
    "field_routing",
    "musical_coherence",
    "title_narrative_hook",
    "language_singability",
    "structure_completion",
    "main_vs_exclusion",
    "playlist_fit_differentiation",
    "premise_and_causality",
    "narrative_verisimilitude",
    "scene_and_timeline_continuity",
    "speaker_addressee_consistency",
    "line_level_semantics",
)
CONTENT_CRITERIA = CRITERIA[-5:]


def valid_review() -> dict[str, object]:
    criteria = {}
    for key in CRITERIA:
        evidence_count = 3 if key == "line_level_semantics" else 2 if key in CONTENT_CRITERIA else 1
        criteria[key] = {
            "score": 2,
            "evidence": [f"{key} evidence {index}" for index in range(evidence_count)],
        }
    return {
        "schema_version": "1.0",
        "track_id": 2,
        "reviewer": "independent-reviewer-1",
        "independent": True,
        "lyrics_sha256": hashlib.sha256(LYRICS.encode("utf-8")).hexdigest(),
        "criteria": criteria,
        "contradictions": [],
        "verisimilitude_breaks": [],
        "unexplained_images": [],
        "status": "PASS",
    }


class LyricReviewValidatorTests(unittest.TestCase):
    def run_validator(self, review: dict[str, object]) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            review_path = root / "review.json"
            output_path = root / "track.md"
            review_path.write_text(json.dumps(review), encoding="utf-8")
            output_path.write_text(OUTPUT, encoding="utf-8")
            return subprocess.run(
                [
                    sys.executable,
                    str(VALIDATOR),
                    str(review_path),
                    "--output",
                    str(output_path),
                    "--track",
                    "2",
                ],
                capture_output=True,
                check=False,
                text=True,
            )

    def test_accepts_bound_independent_content_review(self) -> None:
        result = self.run_validator(valid_review())
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("LYRIC CONTENT PASS", result.stdout)

    def test_rejects_stale_lyrics_hash(self) -> None:
        review = valid_review()
        review["lyrics_sha256"] = "0" * 64
        result = self.run_validator(review)
        self.assertEqual(result.returncode, 1)
        self.assertIn("lyrics_sha256 does not match", result.stdout)

    def test_rejects_open_contradiction_or_unexplained_image(self) -> None:
        for field in ("contradictions", "verisimilitude_breaks", "unexplained_images"):
            with self.subTest(field=field):
                review = valid_review()
                review[field] = ["unresolved content problem"]
                result = self.run_validator(review)
                self.assertEqual(result.returncode, 1)
                self.assertIn(f"{field} must be empty", result.stdout)

    def test_requires_full_scores_for_content_criteria(self) -> None:
        review = valid_review()
        criteria = review["criteria"]
        assert isinstance(criteria, dict)
        for name in ("premise_and_causality", "narrative_verisimilitude"):
            with self.subTest(name=name):
                review = valid_review()
                criteria = review["criteria"]
                assert isinstance(criteria, dict)
                criterion = criteria[name]
                assert isinstance(criterion, dict)
                criterion["score"] = 1
                result = self.run_validator(review)
                self.assertEqual(result.returncode, 1)
                self.assertIn(f"{name} must score 2", result.stdout)

    def test_requires_line_level_evidence_depth(self) -> None:
        review = valid_review()
        criteria = review["criteria"]
        assert isinstance(criteria, dict)
        criterion = criteria["line_level_semantics"]
        assert isinstance(criterion, dict)
        criterion["evidence"] = ["one example is not enough"]
        result = self.run_validator(review)
        self.assertEqual(result.returncode, 1)
        self.assertIn("line_level_semantics requires at least 3 evidence items", result.stdout)


if __name__ == "__main__":
    unittest.main()
