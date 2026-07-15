# Music Design Rules

## Genre Coordinates And Priority

Define genre as `country/region -> era -> market/cultural zone -> macro-genre -> subgenre -> tempo/groove -> language -> production grammar`. Even when the high-level genre name is the same, treat it as a separate coordinate if country, era, rhythm, harmony, instrumentation, or mix grammar differs.

Use the following priority order.

1. The user's latest explicit instruction and approved constraints
2. The Primary reference's musical identity
3. Audible evidence from a Target render approved by the user
4. Natural variation within the central genre and adjacent genres
5. Fine adjustment for the listening situation

A Target render does not automatically replace the Primary reference. Use it as more specific evidence only for the traits the user has identified as the target.

## Fixed Axes And Variation Axes

Maintain the following across all tracks.

- Overall mood and style world
- Central genre and natural adjacent-genre range
- 1-2 common core instruments or production textures
- Approved lead-vocal roster and mix/space standards
- A tempo zone appropriate to the situation

Change the following for each track.

- Combination, role, register, and playing technique of central/supporting instruments
- Intro length and first vocal-entry method
- Kick, snare, hi-hat pattern, syncopation, fills, ghost notes, and accents
- Chord progression and track-specific harmonic device
- Melodic hook, rhythmic contour, narrative, and imagery

Even when reusing the same instrument, change at least one of its role, register, effect, or playing technique. By default, use a genre blend of 70-80% central genre and 20-30% adjacent genre, unless the reference requires otherwise. Do not leap to a weakly related genre.

## Harmony Research

Research at least three real songs close to each track's genre coordinate. Match country, era, subgenre, and language zone as closely as possible, and confirm chord or harmonic features from accessible reliable sources. Do not present unverifiable progressions as facts; mark uncertainty.

Compare common progressions, cadences, modal traits, bass movement, and section transitions, then design a new progression. Do not copy one song's exact progression wholesale. Use at least one genre-appropriate device such as substitute chords, borrowed chords, secondary dominants, inversions, turnarounds, or optional modulation.

Harmony references must also come only from songs whose primary lyric language is English, Japanese, or Korean. Overlap among Primary, Supporting, and general auxiliary references is allowed. Each track must use at least three harmony references, and only partial overlap is allowed across tracks. For two track lists `A` and `B`, an overlap of `|A intersection B| / min(|A|, |B|)` at 50% or above is a conflict. If each list contains three songs, one shared song is allowed and two shared songs are not. During every revision, compare the current track pairwise against all other tracks; if overlap is 50% or above, replace only the conflict-causing harmony references with different real songs from the allowed language pool, then revalidate the chord design. Use real song and artist names only as design evidence, not in the Suno Prompt.

## Separate Dynamic Axes

Do not collapse the following values into one.

| Axis | Meaning | Default treatment |
|---|---|---|
| Energy 3/4/5 | Relative momentum within the playlist | Center on 4, balance 3 and 5 |
| Arrangement dynamics | Section-level loudness, density, drums, and layer curve | Preserve the genre's natural structure |
| Vocal emotional depth | Depth of emotional expression in the vocal | Match lyrics and situation |
| Vocal lowest note | Lowest note of the lead melody | Specify within the approved range |

If the user defines "dynamics" as emotional depth plus vocal lowest note, do not alter Arrangement dynamics. Do not translate `low emotional dynamic` into `flat arrangement`, `no chorus lift`, `no fills`, or `no layer growth`. Use those restrictions only when the user explicitly applies them to the arrangement axis.

## Structure, Hook, And Length

Use `Intro -> Verse 1 -> Pre-Chorus -> Chorus -> Verse 2 -> Pre-Chorus -> Chorus -> Bridge -> Final Chorus -> Outro` as the default narrative arc, then shorten or reshape it for the genre. Design the emotional arc as situation setup -> rise -> core message -> turn/climax -> resolution.

For every 10-track full design, randomly assign each track one hook strategy from the following candidates.

- `No hook`: chorus narrative and melody develop each time
- `Repeated hook`: a short line or melody returns 2-3 times
- `Varied chorus`: the same central thought changes through lyric, register, or rhythm
- `Final-only callback`: the title or key phrase appears only in the final chorus
- `Instrumental hook`: an instrument or rhythmic motif carries the memorable point without a lyric hook

If one strategy exceeds three tracks out of ten, or the same strategy appears three tracks in a row, reroll only that track. If the selected result conflicts with the track's narrative or genre, do not arbitrarily assign another strategy; reroll. The random assignment determines only the hook method. The actual line, melody, and rhythm must be newly designed for each track.

When a repeated strategy is selected, vary at least one of lyric, register, harmony, rhythm, or instrument on each repetition. Do not fix absolute runtime; target +/-20% of the genre-standard length. Calculate lyric volume from BPM, syllable density, intro, interlude, outro, and selected hook strategy.

## Language And Vocals

Use English as the default, with Japanese and Korean as auxiliary options. Use only one language per track, and align title, hook, and lyrics. Confirm language as part of the genre coordinate.

The playlist may have up to three leads, but if the user specifies one vocalist, use exactly that one. Each track has a single lead. Background chorus and harmony are allowed according to user constraints and track design, but do not design them so they sound like an alternate lead.

## Exclusions

Choose only exclusions required for the track's purpose, such as no vocal before a specific bar, or excluding a specific genre, instrument, vocal technique, or mix trait. Do not automatically turn an example into a playlist-wide rule.

If the user decides that mentioning a forbidden concept itself induces the unwanted result, remove that word from both positive and negative wording and use only positive replacement language for the desired sound. Do not let the exclusion list become longer than the desired style description.
