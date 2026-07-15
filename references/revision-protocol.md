# Approval And Revision Protocol

## Maintain State

Keep the following briefly in the conversation state.

- Approved genre coordinates, reference DNA, and vocal roster
- Approved 10-track full design table
- Real supporting references and harmony references used per track
- Approved tracks and tracks not yet created
- Accumulated common requirements

Allow the same general supporting reference to appear across multiple tracks. Select at least three real harmony references from the allowed English-language pop, Japanese-language, and Korean-language pools. Partial overlap in harmony references across tracks is allowed, but overlap of 50% or more between any two tracks is not allowed. Record the role and application scope of any repeated song in the full design table.

## Distinguish Reset From Track-Level Redesign

When the user explicitly says `reset`, `full reset`, `complete reset`, `project reset`, or `playlist reset`, always treat it as a full reset. Do not reduce it to regenerating the current track or partially clearing state.

On reset, transition state in this order.

1. Leave the current approved state, per-track versions, and feedback in history as `pre-reset archive`. Do not delete or overwrite them.
2. Clear all active Context, Primary/Supporting references, Target/Rejected renders, Approved constraints, genre coordinates, language, vocal roster and voicing, exclusions, and accumulated common rules.
3. Clear the previous 10-track design table and approval, current track selection, per-track generation order, and Prompt/Lyrics completion state. Do not use pre-reset values as defaults or assumptions for the new project.
4. Restart the initial interview from the new project's Context and Primary reference. Ask only 1-2 questions at a time, and do not restore prior answers unless the user states them again.
5. Once high-level input and vocal approval are in place, write exactly 10 rows in the new full design table. Request approval for the new design and stop. Before approval, do not output any single-track Suno Prompt or Lyrics.

`Redesign the current track from scratch`, `fully revise this track`, and `rewrite the Prompt and Lyrics` are track-level full regenerations. Those phrases alone do not cancel approval of the 10-track design. Clarify only when `from scratch` is ambiguous between project-level and current-track scope and the result would materially differ.

## Interview Why The User Dislikes It

When the user asks for a change or regeneration, do not immediately recreate the track. Ask follow-up questions 1-2 at a time until the dissatisfaction is specific enough. Do not ask again about details the user has already answered specifically.

Probe these axes as needed.

- Is reference similarity too high or too low?
- Are any genre-coordinate interpretations wrong: country, era, subgenre, language, or speed?
- Is the issue vocal timbre, voicing, lowest note, emotional depth, breath, or accent?
- Is the issue instrumentation, intro, drum performance, chord progression, or unique harmonic device?
- Is the issue hook memorability, repetition count, melodic density, or song structure?
- Is the issue lyric topic, point of view, narrative, language, expression intensity, or syllable density?
- Is the issue length, energy, mix, space, or fit for the listening situation?
- Is it too similar to another track or outside the playlist world?

If the user says vague things like "not good," "different," or "better," ask for the concrete audible trait and the desired opposite direction. If the user provides sufficiently specific revision instructions, end the interview and regenerate. If the user explicitly requests immediate regeneration, proceed with the confirmed information only.

## Distinguish Track-Specific Revisions From Common Revisions

If the change applies only to the current track, treat it as a track-specific revision. Redesign the current track's integrated Suno Prompt and Lyrics together, and do not change other tracks.

If the change applies to the current track and all remaining tracks, treat it as a common revision. Add it to accumulated common requirements and regenerate the current track. Apply it to remaining track designs, but do not change already approved tracks unless the user asks.

Clarify whether it is current-track-only or common only when the distinction is ambiguous and would materially change the result.

## Regenerate

1. Briefly restate the confirmed dissatisfaction and goal in Korean.
2. Classify it as track-specific or common.
3. Do not use the existing prompt as an editing source. Rejudge style and lyrics from the approved full design and latest requirements from scratch.
4. Completely refactor and re-output the whole integrated Suno Prompt and Lyrics, removing failed expressions, discarded conditions, and conflicting/duplicated phrases. Do not provide only partial phrases, differences, or add-on instructions.
5. Check the integrated Suno Prompt for 800 characters, integrated exclusions, no positive/negative instruction conflict, single lyric language, genre-standard runtime +/-20%, vocal consistency, repeated-reference roles/application scope, and harmony-reference overlap below 50%.
6. If it is a common revision, state the accumulated rule that will apply to subsequent tracks in one line.
7. Add the revision reason, classification, new check result, and new integrated prompt as a new version in the relevant `history/YYYY-MM-DD__topic-slug.md`, and maintain the root `PROJECT_HISTORY.md` index.

In every revision, compare the current track's at least three confirmed harmony references pairwise against every other track's confirmed or planned list. Do not skip this check even if the harmony itself did not change. If `intersection count / shorter list count` is below 50%, allow the overlap; if it is 50% or above, replace only the conflict-causing item(s) and calculate again. For each repeated song, record the harmonic element referenced by the current track and how its role differs from other tracks.

Do not create mismatched results by changing only fragments. Every revision must be a complete refactored version. Keep improving the same track until the user approves it, and move to the next track only after approval.
