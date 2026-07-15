# Approval And Revision Protocol

## Maintain State

Keep the following briefly in the conversation state.

- Approved genre coordinates, reference DNA, Playlist sound contract, Form Evidence Table, Permitted Variation Envelopes, Structural Flow Contracts, Lyrics tag sequences, Vocal And Engineering Contract, Calibration Lock, and vocal roster
- Approved 10-track full design table, including each track's differentiator, verified form/source, permitted sequence, and development signature
- Real supporting references and harmony references used per track
- Current track, its Main Prompt A/B/C, shared Exclusion Prompt, shared Title And Lyrics, chosen Main Prompt, approved track sets, and remaining ungenerated tracks
- Accumulated common requirements

Allow the same general supporting reference to appear across multiple tracks. Select at least three real harmony references from the allowed English-language pop, Japanese-language, and Korean-language pools. Partial overlap in harmony references across tracks is allowed, but overlap of 50% or more between any two tracks is not allowed. Record the role and application scope of any repeated song in the full design table.

## Distinguish Reset From Track-Level Redesign

When the user explicitly says `reset`, `full reset`, `complete reset`, `project reset`, or `playlist reset`, always treat it as a full reset. Do not reduce it to regenerating the current track or partially clearing state.

On reset, transition state in this order.

1. Leave the current approved state, per-track versions, and feedback in history as `pre-reset archive`. Do not delete or overwrite them.
2. Clear all active Context, the Playlist sound contract, form evidence, variation envelopes, Structural Flow Contracts, Lyrics tag sequences, Vocal And Engineering Contract, Calibration Lock, Primary/Supporting references, Target/Rejected renders, Approved constraints, genre coordinates, language, vocal roster and voicing, exclusions, and accumulated common rules.
3. Clear the previous 10-track design table and approval, current-track selection, track-by-track approval order, every Main Prompt A/B/C and chosen prompt, and all shared Exclusion Prompt and Title And Lyrics completion states. Do not use pre-reset values as defaults or assumptions for the new project.
4. Restart the initial interview from the new project's Context and Primary reference. Ask only 1-2 questions at a time, and do not restore prior answers unless the user states them again.
5. Once high-level input, form evidence, variation envelopes, Structural Flow Contracts, Lyrics tag sequences, and vocal approval are in place, write exactly 10 rows in the new full design table. Request approval for the new design and stop. Before approval, do not output any Main Prompt, Exclusion Prompt, or Title And Lyrics.

`Redesign the current track from scratch`, `fully revise this track`, and `rewrite the current track set` are track-level full regenerations. Those phrases alone do not cancel approval of the 10-track design. Clarify only when `from scratch` is ambiguous between project-level and current-track scope and the result would materially differ.

## Interview Why The User Dislikes It

When the user asks for a change or regeneration, do not immediately recreate the track. Ask follow-up questions 1-2 at a time until the dissatisfaction is specific enough. Do not ask again about details the user has already answered specifically.

Probe these axes as needed.

- Is reference similarity too high or too low?
- Are any genre-coordinate interpretations wrong: country, era, subgenre, language, or speed?
- Is the issue vocal timbre, voicing, lowest note, emotional depth, breath, or accent?
- Does the voice sound artificial because of formant wobble, metallic resonance, pitch stepping, smeared consonants, phasey doubling, clipped breaths, or another audible symptom?
- Is the issue instrumentation, intro, drum performance, chord progression, or unique harmonic device?
- Is the issue the verified form, a permitted-variation boundary, Structural Flow Contract, section sequence, Lyrics tag sequence, first entry, peak placement, contrast mechanism, or ending behavior?
- Is the issue hook memorability, repetition count, melodic density, or compatibility with the approved structure?
- Is the issue lyric topic, point of view, narrative, language, expression intensity, or syllable density?
- Is the issue length, energy, mix, space, or fit for the listening situation?
- Is it too similar to another track or outside the playlist world?

If the user says vague things like "not good," "different," or "better," ask for the concrete audible trait and the desired opposite direction. If the user provides sufficiently specific revision instructions, end the interview and regenerate. If the user explicitly requests immediate regeneration, proceed with the confirmed information only.

## Distinguish Track-Specific Revisions From Common Revisions

Classify every correction with one scope.

- `track-local`: current track only; do not add it to the Calibration Lock
- `next-track-only`: apply it to the next track, record expiry, then remove it after that track's approval
- `remaining-common`: add it to the Calibration Lock and apply it to every remaining ungenerated track
- `project-global`: use only when the user explicitly applies it to the whole project; revise approved tracks only when explicitly requested

A chosen A/B/C preference defaults to `remaining-common` unless it depends on a unique current-track trait or the user narrows the scope.

For a track-local revision, regenerate Main Prompt A/B/C and revalidate the shared Exclusion Prompt and Title And Lyrics. Rewrite a shared field only when the feedback targets it. Do not change other tracks.

For a remaining-common revision, add it to accumulated common requirements and the Calibration Lock, regenerate the current track, and update the remaining track designs inside their approved form envelopes. Do not change already approved tracks unless the user asks.

Clarify whether it is current-track-only or common only when the distinction is ambiguous and would materially change the result.

## Regenerate

1. Briefly restate the confirmed dissatisfaction and goal in Korean.
2. Classify it as track-specific or common.
3. Do not use the existing outputs as editing sources. Rejudge style and lyrics from the approved full design and latest requirements from scratch.
4. Completely refactor and re-output Main Prompt A/B/C plus the shared Exclusion Prompt and shared Title And Lyrics, removing failed expressions, discarded conditions, and conflicting or duplicated phrases. Do not provide only partial phrases, differences, or add-on instructions.
5. Check all three Main Prompts for 800 characters each, the shared Exclusion Prompt for 100 characters, no cross-prompt conflict or duplicated exclusion, single lyric language, genre-standard runtime +/-20%, Playlist sound contract fit, verified form evidence, permitted-variation and Structural Flow compliance, exact Lyrics tag sequence, vocal consistency, repeated-reference roles/application scope, and harmony-reference overlap below 50%.
6. If it is a common revision, state the accumulated rule that will apply to all remaining ungenerated tracks in one line.
7. Add the revision reason, classification, controlled A/B/C axes, chosen Main Prompt, audible evidence, Calibration Lock update, any structure/development change, check result, and the complete current-track set as a new version in the relevant `history/YYYY-MM-DD__topic-slug.md`. Maintain the root `PROJECT_HISTORY.md` index.

In every revision, compare the current track's at least three confirmed harmony references pairwise against every other track's confirmed or planned list. Do not skip this check even if the harmony itself did not change. If `intersection count / shorter list count` is below 50%, allow the overlap; if it is 50% or above, replace only the conflict-causing item(s) and calculate again. For each repeated song, record the harmonic element referenced by the current track and how its role differs from other tracks.

Do not create mismatched results by changing only fragments. Every revision must present all three Main Prompts and the one shared Exclusion Prompt and Title And Lyrics. Keep improving the same track until the user approves one Main Prompt, update the Calibration Lock, and only then move to the next track.
