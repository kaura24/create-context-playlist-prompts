from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_track_output.py"
FIELDS = (
    "Style: Korean indie neo-soul; "
    "Feel: warm rainy desk-reading, low arousal; "
    "Tempo/Groove: 76 BPM, 4/4 loose pocket; "
    "Vocal: Korean alto V1, close dry center, stable formants; "
    "Instrumentation: Rhodes, muted guitar, round bass, soft kick, brushed rim; "
    "Harmony: Verse Am9-D13-Gmaj7-Cmaj7; Refrain Fmaj7-G6-Em7-Am9; "
    "Form/Flow: verse-refrain with bridge, restrained final release; "
    "Production/Mix: small room, gentle saturation, soft transients."
)


def output_text(main_a: str = FIELDS, main_b: str | None = None, main_c: str | None = None) -> str:
    main_b = main_b or FIELDS.replace("Fmaj7-G6", "Fm6-G6")
    main_c = main_c or FIELDS.replace("restrained final release", "extended bridge release")
    return f"""| Main Prompt | Constants | Test axis 1 | Expected audible difference |
|---|---|---|---|
| A | fixed scaffold | baseline | reference point |
| B | fixed scaffold | harmonic color | darker return |
| C | fixed scaffold | bridge release | longer release |

**Main Prompt A**
```text
{main_a}
```

**Main Prompt B**
```text
{main_b}
```

**Main Prompt C**
```text
{main_c}
```

**Exclusion Prompt**
```text
metallic vocals, formant wobble, trap hats
```

**Title And Lyrics**
```text
Title: Window Light

[Intro]
Rain on the glass

[Verse]
I turn one page

[Refrain]
The low light stays

[Outro]
The room grows still
```
"""


class ValidatorTests(unittest.TestCase):
    def run_validator(self, text: str) -> subprocess.CompletedProcess[str]:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md") as handle:
            handle.write(text)
            handle.flush()
            return subprocess.run(
                [
                    sys.executable,
                    str(VALIDATOR),
                    handle.name,
                    "--expected-tags",
                    "Intro,Verse,Refrain,Outro",
                ],
                capture_output=True,
                check=False,
                text=True,
            )

    def test_accepts_valid_output(self) -> None:
        result = self.run_validator(output_text())
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS:", result.stdout)

    def test_rejects_overlong_main_prompt(self) -> None:
        result = self.run_validator(output_text(main_a=FIELDS + " x" * 500))
        self.assertEqual(result.returncode, 1)
        self.assertIn("maximum is 800", result.stdout)

    def test_rejects_brackets_and_negative_command_in_main_prompt(self) -> None:
        result = self.run_validator(output_text(main_b=FIELDS + " [Chorus] no trap hats"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("contains bracketed text", result.stdout)
        self.assertIn("negative command", result.stdout)

    def test_rejects_identical_wording_and_unsupported_lyrics_tag(self) -> None:
        text = output_text().replace("fixed scaffold", "identical sound", 1)
        text = text.replace("[Refrain]", "[First Window]", 1)
        result = self.run_validator(text)
        self.assertEqual(result.returncode, 1)
        self.assertIn("same or identical", result.stdout)
        self.assertIn("Unsupported Lyrics tags", result.stdout)


if __name__ == "__main__":
    unittest.main()
