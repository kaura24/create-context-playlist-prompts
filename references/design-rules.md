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

## Translate Context Into A Playlist Sound Contract

Treat Context as the listening function and emotional setting, not as a genre label. Before designing tracks, summarize the approved contract as:

`Use case | Common sound | Track variation pool | Drift boundaries`

### Common Sound

Maintain the following across all tracks.

- The listening purpose, overall mood, and arousal envelope
- Central genre and natural adjacent-genre range
- Brightness, density, transient character, and arrangement-dynamics range
- 1-2 common core instruments or production textures
- Approved lead-vocal roster, vocal distance, and mix/space standards
- A tempo and groove zone appropriate to the situation

Translate contextual language into audible traits only when the link is justified. For example, rain may support muted transients, close ambience, or restrained high-frequency detail, but it does not require literal rain sound effects.

### Track Variation

Change the following within the Common sound.

- Track-specific scene, narrative, imagery, and emotional turn
- Structure family, section development, peak placement, and ending behavior
- Combination, role, register, effect, and playing technique of central/supporting instruments
- Intro length, first vocal entry, and transition method
- Kick, snare, hi-hat pattern, syncopation, fills, ghost notes, and accents
- Chord progression, harmonic color, and track-specific harmonic device
- Melodic contour, rhythmic motif, and compatible hook strategy

Even when reusing the same instrument, change at least one of its role, register, effect, or playing technique. By default, use a genre blend of 70-80% central genre and 20-30% adjacent genre, unless the reference requires otherwise. Do not leap to a weakly related genre.

Before approval, ask internally: `Does each track vary within the shared use case rather than reinventing it?` If not, revise the track or the contract before showing the table.

## Harmony Research

Research at least three real songs close to each track's genre coordinate. Match country, era, subgenre, and language zone as closely as possible, and confirm chord or harmonic features from accessible reliable sources. Do not present unverifiable progressions as facts; mark uncertainty.

Compare common progressions, cadences, modal traits, bass movement, and section transitions, then design a new progression. Do not copy one song's exact progression wholesale. Use at least one genre-appropriate device such as substitute chords, borrowed chords, secondary dominants, inversions, turnarounds, or optional modulation.

Harmony references must also come only from songs whose primary lyric language is English, Japanese, or Korean. Overlap among Primary, Supporting, and general auxiliary references is allowed. Each track must use at least three harmony references, and only partial overlap is allowed across tracks. For two track lists `A` and `B`, an overlap of `|A intersection B| / min(|A|, |B|)` at 50% or above is a conflict. If each list contains three songs, one shared song is allowed and two shared songs are not. During every revision, compare the current track pairwise against all other tracks; if overlap is 50% or above, replace only the conflict-causing harmony references with different real songs from the allowed language pool, then revalidate the chord design. Use real song and artist names only as design evidence, not in the Main Prompt or Exclusion Prompt.

## Separate Dynamic Axes

Do not collapse the following values into one.

| Axis | Meaning | Default treatment |
|---|---|---|
| Energy 3/4/5 | Relative momentum within the playlist | Center on 4, balance 3 and 5 |
| Arrangement dynamics | Section-level loudness, density, drums, and layer curve | Preserve the genre's natural structure |
| Vocal emotional depth | Depth of emotional expression in the vocal | Match lyrics and situation |
| Vocal lowest note | Lowest note of the lead melody | Specify within the approved range |

If the user defines "dynamics" as emotional depth plus vocal lowest note, do not alter Arrangement dynamics. Do not translate `low emotional dynamic` into `flat arrangement`, `no chorus lift`, `no fills`, or `no layer growth`. Use those restrictions only when the user explicitly applies them to the arrangement axis.

## Hook And Length

Choose every track's structure family and development signature through [structure-patterns.md](structure-patterns.md) before assigning its hook. The structure constrains the compatible hook candidates; hook randomization must not rewrite the structure after the fact.

For every 10-track full design, randomly draw each track one compatible hook strategy from the following candidates.

- `No hook`: the narrative and melody develop without a recurring focal phrase
- `Repeated hook`: a short line or melody returns 2-3 times
- `Varied return`: the same central thought changes through lyric, register, harmony, or rhythm at each return
- `Final-only callback`: the title or key phrase appears only in the closing return or section
- `Instrumental hook`: an instrument or rhythmic motif carries the memorable point without a lyric hook

If one strategy exceeds three tracks out of ten, or the same strategy appears three tracks in a row, reroll only that track. If the selected result conflicts with the track's narrative or genre, do not arbitrarily assign another strategy; reroll. The random assignment determines only the hook method. The actual line, melody, and rhythm must be newly designed for each track.

When a repeated strategy is selected, vary at least one of lyric, register, harmony, rhythm, or instrument on each repetition. Do not fix absolute runtime; target +/-20% of the genre-standard length. Calculate lyric volume from BPM, syllable density, approved section sequence, intro, interlude, outro, and selected hook strategy.

## Language And Vocals

Use English as the default, with Japanese and Korean as auxiliary options. Use only one language per track, and align title, hook, and lyrics. Confirm language as part of the genre coordinate.

The playlist may have up to three leads, but if the user specifies one vocalist, use exactly that one. Each track has a single lead. Background chorus and harmony are allowed according to user constraints and track design, but do not design them so they sound like an alternate lead.

## Exclusions

Choose only absolute exclusions required for the track's purpose, such as no vocal before a specific bar, or excluding a specific genre, instrument, vocal technique, or mix trait. Do not automatically turn an example into a playlist-wide rule. The final Exclusion Prompt must fit within 100 characters including spaces and punctuation.

If the user decides that mentioning a forbidden concept itself induces the unwanted result, remove that word from both the Main Prompt and Exclusion Prompt and use only positive replacement language for the desired sound. Do not duplicate an exclusion across both prompts.
