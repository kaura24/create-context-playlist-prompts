# Playlist And Track Design Rules

Design from shared function to individual track detail. Keep the source of truth in PlaylistSpec, not in a wide conversational table.

## Create The Playlist Contract

Summarize:

| Use case | Common sound | Variation pool | Drift boundaries |
|---|---|---|---|

Keep the listening function, central genre, lyric-language policy, arrangement dynamic range, percussion role, core vocal identity, vocal high-note policy, and mix world coherent. Vary narrative, form realization, opening signature, groove signature, instrumentation role, harmony, hook method, peak, and ending.

## Research Three Real Songs Per Track

Browse before reserving slots and assign exactly three distinct real, existing songs to each track: `structure`, `harmony`, and `emotional_arc`, for 30 role-bound references overall. Record artist, track, HTTP(S) URL, role, and the high-level trait distilled from the inspected source. Do not accept three names without extraction. Take section logic only from the structure song; tonal-center behavior, harmonic rhythm, cadence, bass motion, and color from the harmony song; and tension-turn-release logic from the emotional-arc song. Choose exactly one of the three as a secondary hook-melody model and mark that binding's `distilled_trait` with `Hook model:`. Extract motif length, contour class, rhythmic cell, title placement, and return pattern, then create a new note sequence, interval order, rhythm variation, and lyric stress pattern—never its actual melody. Synthesize a new design without copying exact progression, melody, hook, lyrics, signature riff, or source-specific imagery; keep all 10 `Harmony` fields unique.

## Create A Concise 10-Track Map

Use exactly 10 rows:

| # | Working title | Scene and emotional turn | Genre/groove | Form and planned duration | Differentiator | Vocal/language | Status |
|---|---|---|---|---|---|---|---|

Derive every row from one of the 10 bound PlaylistSpec tracks. Make rows audibly distinct without changing the Playlist Contract. Keep detailed chords, sources, and engineering fields in the nested TrackSpecs.

## Design Each Track In One Direction

Use this order:

1. Consume one validated reserved slot; do not choose a new form, sequence, opening signature, or groove signature.
2. Preserve its locked fingerprint and write matching plain-prose `Form/Flow`.
3. Define each section's musical job and transition.
4. Assign bars and vocal flags without changing the locked tag sequence.
5. Realize the locked hook-return behavior with original material.
6. Design section-level harmony and bass motion.
7. Assign instrument, drum, vocal, and mix behavior.

Never rename an observed sequence as an established form. When evidence is weak, retain the literal sequence and label it provisional. Research is required only for claims about real songs, established form names, release facts, or source-specific harmony.

## Plan 3-4 Minute Structure

Set target_duration_seconds inside 180-240 seconds and prefer 195-225 seconds. Record BPM and the metrical pulse represented by BPM. Calculate planned time from total bars.

Example at 96 BPM with four metrical pulses per bar:

    84 bars × 4 × 60 / 96 = 210 seconds

Allocate bars across intro, vocal sections, instrumental contrast, return, and ending. Keep the bar plan and lyric tags aligned. A valid bar plan proves planned duration only; generated audio establishes actual duration.

## Size Complete Lyrics

Write every return in full. Avoid shorthand such as x2 or repeat chorus. Give every vocal section performable lines and enough language-specific lyric units for its bars.

- English: count words as a conservative unit.
- Korean: count Hangul syllable blocks; allow limited English hook words.
- Japanese: count kana and kanji characters as a conservative readiness proxy.

Use density bounds as a structural plausibility check. Treat pronunciation, melisma, held notes, rap density, and actual timing as semantic or render evidence.

## Design Original Harmony And Hooks

Use references to learn high-level harmonic language, cadence behavior, groove, and arrangement roles. Create a new section-level progression rather than copying one reference wholesale. Use borrowed color, inversions, secondary dominants, modal motion, or modulation only when the genre and narrative support it.

Do not require an arbitrary number of harmony references. When the task explicitly requests research, record each reference's role and avoid overusing one source across the playlist.

Choose one compatible hook approach and realize the named hook-melody model as an original low-dimensional motif. Preserve only its catchiness mechanism, not pitches or signature timing. Random hook prominence is a separate bounded axis: use the balanced shuffled bag and recorded seed, encode the assigned level in `Form/Flow`, and preserve the selected structure. It does not override locked hook-return behavior or dynamic locks. Strong means memorable repetition, rhythm, contour, or wording—not automatically louder or higher:

- no recurring hook
- repeated hook
- varied return
- final-only callback
- instrumental hook

Change the actual line, melody concept, rhythm, and harmony for every track.

## Keep Dynamic Axes Separate

- Playlist energy: relative momentum among tracks
- Arrangement dynamics: section density, loudness, drums, and layers
- Vocal emotional depth: performed emotional intensity
- Vocal lowest note: lower boundary of the lead melody
- Vocal highest note and high-note policy: upper boundary plus low-register/no climax, one controlled high peak, or open range; peak via pitch, harmony, rhythm, density, timbre, or space
- Percussion role: support-only or percussion-led; require explicit opt-in for percussion-led and never use it merely to manufacture playlist variety

Never use `low dynamics` as a complete instruction. Resolve arrangement movement and vocal pitch independently, then state how the climax changes without violating either lock. When support-only is selected, keep drums subordinate and omit percussion-led from Style and differentiators. Apply feedback only to the named axis. Do not flatten arrangement movement because the user requests restrained vocal emotion, and do not retain high vocal peaks when the user lowers overall dynamics unless they explicitly preserve them.

## Keep One Lead Identity

Use one lead per track. If the user names one vocalist or voice identity, retain it across the playlist. Keep background harmony subordinate. Specify range, lowest note, vocal highest note, high-note policy, register, timbre, phrasing, pronunciation, phrase joins, emotion, mic distance, and rejected artifacts only to the level supported by the request.

Translate vague terms such as natural or non-AI into audible behavior: stable formants, continuous vowels, clear consonants, clean phrase joins, controlled vibrato, centered lead, and preserved phrase dynamics. Under an artifact-token suppression lock, remove the named family and adjacent performance or capture cues instead of describing the unwanted sound in any active field.

## Check Playlist Coherence

Before compilation, verify:

- Every track serves the use case.
- All 10 TrackSpecs remain bound to distinct validated slots and exactly three role-bound real-song HTTP(S) references per slot; exactly one binding per new track is named as its hook-melody model, and `Form/Flow` describes the newly composed motif without artist or song names.
- Every differentiator changes an audible dimension.
- Form, hook, and lyric tags agree.
- Planned time is 180-240 seconds.
- Every opening and groove signature has exactly three pipe-separated clauses; every selected pair must differ on at least two of three axes, all clauses must appear in `Instrumentation`/`Form/Flow` or `Tempo/Groove`, and harmony, groove, and instrument roles avoid duplicates while support-only percussion remains subordinate.
- Every Harmony field follows its slot's reference model without copying its exact progression.
- Language, arrangement range, vocal boundaries, high-note policy, hook prominence, and lead identity match TrackSpec; new musical content does not copy a source's protected expression.
