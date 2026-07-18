# Quality And Render Protocol

Separate deterministic correctness, semantic quality, and audible evidence. Passing one level never implies the next.

## Use Five Evidence Labels

| Label | Evidence |
|---|---|
| planned | TrackSpec exists but has not passed validation |
| PLAN PASS | TrackSpec and compiled text pass deterministic checks |
| draft-validated | PLAN PASS plus passing semantic and bound lyric-content reviews |
| render-duration-verified | Supplied audio metadata is 180-240 seconds |
| render-verified | Duration and the semantic listening rubric pass |

Continue drafting after PLAN PASS when audio is unavailable. State the evidence boundary instead of turning it into a serial blocker.

## Run Deterministic Checks

Use validate_track_output.py in playlist-bound mode; use standalone TrackSpec mode only for a single-track request. Treat these as hard failures:

- malformed or contradictory TrackSpec
- planned duration outside 180-240 seconds
- missing requested code block, outside title, field, section, tag, or vocal lyrics
- prompt or exclusion character overflow
- Basic Prompt text that does not compile exactly from TrackSpec
- placeholder or repeat shorthand
- clear selected-language mismatch

Repair these internally before delivery. Keep uncertain lyric density and mixed-language nuance conservative; do not claim precise sung timing from text alone.

## Score Semantic Quality

After PLAN PASS, score each item from 0 to 2:

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Design traceability | contradicts TrackSpec | partial | every major choice traces |
| Field routing and output contract | mixed or malformed | minor leak | three clean paste-ready fields and outside title |
| Musical coherence | conflicting | usable | form, harmony, groove, and mix reinforce |
| Title, narrative, and hook | generic or inconsistent | serviceable | distinctive and aligned |
| Language and singability | broken | uneven | natural, performable phrasing |
| Structure and lyric completion | incomplete | minor weakness | complete and bar-aware |
| Main versus Exclusion | conflict | redundant | clean field separation |
| Playlist fit and differentiation | off-contract | weak distinction | cohesive and clearly differentiated |
| Premise and causality | events do not follow | weak link | every action has a clear reason and consequence |
| Narrative verisimilitude | unearned action or image | weakly prepared | events, choices, and imagery feel true within the established premise, character, and tone |
| Scene and timeline continuity | unexplained jumps | recoverable gap | place, time, and action progress coherently |
| Speaker and addressee consistency | roles shift | slight ambiguity | narrator and addressed person remain stable |
| Line-level semantics | nonsensical imagery | isolated strain | every line has a literal or context-supported meaning |
Require at least 23/26, no zero, and 2 for design traceability, routing, completion, `premise_and_causality`, `narrative_verisimilitude`, `scene_and_timeline_continuity`, `speaker_addressee_consistency`, and `line_level_semantics`. Bind the fresh review with `lyrics_sha256`; require evidence and empty `contradictions`, `verisimilitude_breaks`, and `unexplained_images`, then run `validate_lyric_review.py`. Judge truth within the established premise, not event frequency in ordinary life.

This score tests prompt and lyric quality. It does not prove the generator will follow every instruction. Treat an unconfirmed lead-role label, a direct token, or an adjacent cue that violates an active artifact-suppression lock as a design-traceability and musical-coherence failure; archives are outside this check.

## Measure Render Duration

For a supplied WAV, MP3, M4A, FLAC, or other ffprobe-readable file, run:

    python3 scripts/validate_render.py render-file

Accept 180.000 through 240.000 seconds inclusive. Record measured duration. A bar plan near 195-225 seconds provides useful variance margin but does not replace this measurement.

## Review Audible Quality

Listen to the full file before assigning render-verified. Record:

| Axis | Match, partial, mismatch, or unknown | Evidence |
|---|---|---|
| Lead identity, register, pronunciation, and timing |  |  |
| Basic Prompt is audible and exclusions are absent |  |  |
| Last lyric, form, peak, instruments, and groove follow TrackSpec |  |  |
| Space, tone, low end, and context fit |  |  |

Do not infer an audible match from a prompt or filename.

## Diagnose Artificial Vocals Precisely

Separate identity, performance, language, capture, mix, and generation artifacts. Record the heard symptom, desired opposite, evidence level, affected TrackSpec field, and one causal-axis revision.

## Handle Audio Roles

- Primary reference: overall style grammar
- Supporting reference: one bounded design axis
- Target render: positive audible target for named traits
- Rejected render: counterexample used only for diagnosis

Prioritize a Target render for the disputed audible trait while preserving the Playlist Contract elsewhere. Never claim to have listened when only metadata or a user description is available.

## Batch Calibration Safely

The user may return several renders together. Measure and review them in a batch, update track-local overrides first, and promote only repeated or explicitly broad findings to playlist-lock. Keep later draft production independent from missing render evidence.
