# Handover

## Status

The skill architecture update is implemented but the final validator-driven model integration test was intentionally interrupted on 2026-07-15 at the user's request. Commit and push the current state as the handover checkpoint; do not represent the interrupted integration test as passing.

## Implemented Decisions

- Design exactly 10 tracks and approve the full table before compiling actual track outputs.
- Compile and approve one track at a time so listening feedback can calibrate later tracks.
- Output exactly three Main Prompts A/B/C, one shared Exclusion Prompt, and one shared Title And Lyrics per track.
- Keep title, lyrics, Lyrics tag sequence, lead identity, language, central genre, and absolute exclusions fixed across A/B/C.
- Treat Feel, harmony, form development, Structural Flow, arrangement, and production as similar rather than identical inside approved envelopes.
- Treat similarity as permission for bounded variation, not a requirement to rewrite every eligible field. Only 1-2 declared axes may vary in one comparison round; non-test-axis values remain semantically at the A baseline.
- Compile A directly from the approved track row and active Calibration Lock. B/C are bounded alternatives.
- Put genre and Feel, section-level harmony, plain-prose form/flow, vocal behavior, instrumentation, and audio engineering in each Main Prompt.
- Keep bracketed structural tags out of Main Prompts and use only verified Suno-readable tags in Title And Lyrics.
- Keep each Main Prompt at 800 characters or fewer and the shared Exclusion Prompt at 100 characters or fewer.
- Use evidence-backed musical forms and permitted variation envelopes. Never coin a form or poetic section tag.
- Diagnose artificial vocals as audible performance, pronunciation, capture, mix, or generation-artifact symptoms.
- Record listening corrections with `track-local`, `next-track-only`, `remaining-common`, or `project-global` scope.

## Architecture Added Or Revised

- Reworked form evidence, permitted variation, Structural Flow, and Lyrics tag protocols.
- Added ordered approval dependencies and downstream invalidation rules.
- Added Vocal And Engineering Contract and audible AI-vocal diagnosis.
- Clarified prompt-shaped reference intake and offline `evidence-needed` behavior.
- Replaced arbitrary form and hook quotas with evidence-constrained choices.
- Added a deterministic output validator at `scripts/validate_track_output.py`.
- Added validator regression tests at `tests/test_validate_track_output.py`.

## Verification Completed

- Skill metadata validation: `Skill is valid!`
- Validator unit tests: 4 passed.
- `git diff --check`: passed.
- English-source scan for `SKILL.md`, `references/`, and `agents/`: no Korean source text found.
- Independent read-only architecture review: no high-severity contradiction found. Its two findings were fixed:
  - removed unsupported bracketed bar-count/entry instructions from Lyrics;
  - added arrangement and production to the A/B/C similarity gate.
- Two model output dry runs were intentionally used as negative tests. They exposed over-800 prompts, negative commands in Main Prompts, unsupported output shape, and `same`/`identical` wording. The new validator rejects that malformed output.

## Interrupted Work

The final integration test was started with a model instructed to draft a Track 1 output, run `scripts/validate_track_output.py`, revise until PASS, and return the passing draft. It was terminated before the model wrote or validated the draft because the user requested an immediate handover, commit, push, and stop.

## Resume Checklist

1. Run `python3 -m unittest discover -s tests -v`.
2. Run `python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .`.
3. Run one validator-driven Track 1 integration test using the approved fixture or a new approved track row.
4. Require the model to write a temporary Markdown draft with the exact five headings, then run:

   `python3 scripts/validate_track_output.py <draft-file> --expected-tags <comma-separated-approved-tag-sequence>`

5. Confirm the validator returns PASS before evaluating musical semantics.
6. Manually verify that B/C differ only on the declared 1-2 axes; the validator cannot prove semantic traceability to the approved design.
7. Run `git diff --check` and review repository status before the next commit.

## Residual Risks

- The validator enforces output shape, field presence, character limits, bracket placement, negative-command routing, supported Lyrics tags, and explicit same/identical wording. It cannot determine whether a musical descriptor was truly approved or whether an audible variant stays semantically inside its evidence envelope.
- Live Suno generation and listening calibration have not been run for this architecture.
- Codex CLI emitted unrelated local plugin and MCP authentication warnings during model tests; these did not affect the repository's unit tests or static validation.
