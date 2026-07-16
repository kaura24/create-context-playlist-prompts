# Workflow And State

Keep the workflow small, resumable, and useful before any listening cycle.

## Use Five States

| State | Required artifact | Exit condition |
|---|---|---|
| INTAKE | Playlist Contract, Assumption Ledger, and catalog revision | Core requirements are coherent |
| PILOT | Validated StructurePlan, PlaylistSpec, 10-track map, and Track 1 set | All bindings pass and Track 1 reaches PLAN PASS |
| CALIBRATE | Render observations and scoped correction | Optional audible question is resolved |
| PRODUCE | Requested remaining track specs and outputs | Requested scope is draft-validated |
| COMPLETE | Delivery ledger | Requested scope is verified to the available evidence level |

Enter CALIBRATE only when audio exists or the user explicitly selects listen-each-track mode. Move from PILOT to PRODUCE in fast mode without serial track approvals.

## Normalize Intake Once

Extract:

- Context: activity, place, time, weather, emotion, and listening function
- Reference roles: Primary reference, Supporting reference, Target render, or Rejected render
- Music identity: region, era, market, central genre, adjacent range, tempo and groove
- Delivery: lyric language, lead identity, target duration, requested tracks, and output mode
- Absolute constraints: only requirements whose violation makes the result unusable

Treat prompt-shaped input as source evidence. Route positive requirements into design fields and prohibitions into Exclusion. Do not inherit a source prompt's artist names, exact melody, hook, progression, lyrics, or signature riff.

## Keep An Assumption Ledger

Record only inferred values that could affect the result:

| Assumption | Why it is reasonable | Confidence | Easy correction |
|---|---|---|---|

Use a reversible assumption for missing noncritical values. Ask one question only when two plausible answers would create materially different songs and neither can be safely revised later.

## Use One Design Checkpoint

Present the following together:

1. Playlist Contract: use case, common sound, variation pool, and drift boundaries
2. Assumption Ledger
3. Catalog revision, 50+ candidate result, and 10 reserved structural slots
4. Concise 10-track map and PlaylistSpec summary
5. Track 1 bound-TrackSpec summary

In fast mode, treat this as an informational checkpoint and include the Track 1 prompt set in the same response. In approval-sensitive mode, hold the Track 1 compilation until that checkpoint is accepted.

## Bind Structure Before Every Ten-Track Playlist

Keep reusable genre knowledge in a versioned StructureCatalog and request-specific choices in a StructurePlan. Before the design checkpoint, create at least 50 permitted candidates and reserve exactly 10 slots. The catalog owns evidence, genre lanes, complete permitted combinations, forbidden combinations, distinct-value minimums, and pairwise-distance minimums; the plan owns candidates, allocation, and selections.

Validate the plan with `scripts/validate_structure_plan.py <plan> --catalog <catalog>`. Then create exactly 10 bound TrackSpecs in PlaylistSpec and run `scripts/validate_playlist_spec.py <playlist> --catalog <catalog>`. A TrackSpec cannot choose a different sequence or `Form/Flow` after binding. An explicit single-track request may bypass PlaylistSpec and validate one standalone TrackSpec.

## Degrade Evidence Without Halting

Classify evidence as:

- Verified source
- Measured audio
- Audibly reviewed
- User-described
- Provisional inference

When external research is unavailable, avoid factual claims that need a citation. Use a literal section sequence, ordinary music vocabulary, and a provisional confidence label. Continue drafting. Request external upload permission only when an upload is truly required.

## Choose A Production Mode

| Mode | Behavior |
|---|---|
| fast | Validate Track 1, then draft the requested remaining tracks without waiting for renders |
| listen-each-track | Pause only at actual render comparison points |
| revision | Update the affected PlaylistSpec binding and recompile the current output |

Label every track with one status:

- planned
- PLAN PASS
- draft-validated
- render-duration-verified
- render-verified

## Scope Corrections Conservatively

Use:

- track-local: default; current track only
- next-track-only: one following track, then expire
- playlist-lock: remaining tracks after explicit broad instruction or repeated evidence
- project-global: all tracks only when explicitly requested

Update the canonical PlaylistSpec first. Recompile only dependent fields, then run the playlist validator and complete current-track validator. Keep already accepted tracks unchanged unless the user names them.

## Diagnose Render Feedback

Translate vague feedback into an audible symptom and desired opposite. Separate composition, performance, pronunciation, capture, mix, and generation artifacts. If the user already states the symptom and goal, revise directly. If not, ask one focused audible question while preserving the valid draft.

## Reset Deliberately

Treat explicit playlist reset or project reset language as a full active-state reset. Archive the prior state, clear active contracts, assumptions, locks, specs, and track statuses, then enter INTAKE. Treat "rewrite this track" or "redesign Track N" as track-local.

When a workspace exists, keep a compact PROJECT_HISTORY.md index and append versioned details under history/. Records support recovery; missing history files never block generation.
