# PlaylistSpec, TrackSpec, And Output Contract

For a 10-track playlist, build one canonical PlaylistSpec, validate all bindings, then compile the three paste-ready user fields from the requested bound TrackSpec. An explicit single-track request may use one standalone TrackSpec.

## StructureCatalog And StructurePlan

Keep reusable genre rules and request-specific choices in separate UTF-8 JSON files.

- StructureCatalog has exactly `catalog_revision`, `genre_coordinate`, `evidence`, `genre_lanes`, `variation_envelopes`, and `diversity_contract`.
- Evidence sources are HTTP(S) URLs or explicit `user:` approvals. Every lane, envelope, and candidate references registered evidence IDs. For real-song research, put artist, track, observed structural trait, observed harmonic behavior, and selection reason in the evidence record's `scope`.
- Each envelope lists permitted complete fingerprints and forbidden partial combinations. Never generate a Cartesian product from independent option lists.
- StructurePlan has exactly `catalog_revision`, `candidate_pool`, `selection_contract`, and `selections`; its revision must match the catalog.
- `candidate_pool.minimum_count` is at least 50. The catalog owns distinct-value minimums and minimum pairwise distances for both the pool and selected 10.

Every complete fingerprint contains `genre_lane`, `form_id`, `section_sequence`, `recurrence`, `entry`, `contrast_peak`, `transition_interlude`, `ending`, and `hook_return`. Every selection copies the complete candidate projection into `locked_fingerprint`, identifies one of that candidate's HTTP(S) evidence records as `reference_evidence_id`, and may open only non-structural axes.

## PlaylistSpec Binding Schema

Use schema version `1.0`, the catalog's exact revision, one Playlist Contract, the complete validated StructurePlan, and exactly 10 bound tracks:

    {"schema_version":"1.0", "catalog_revision":"genre-catalog-v1",
     "playlist_contract":{"use_case":"...", "common_sound":"...", "variation_pool":"...", "drift_boundaries":"..."},
     "structure_plan":{"...":"complete plan"},
     "tracks":[{"track_id":1, "slot_id":"S01", "candidate_id":"C017",
                "locked_fingerprint":{"...":"exact selection"}, "spec":{"...":"TrackSpec below"}}]}

Track IDs must be exactly 1 through 10. Each selection needs a candidate-cited HTTP(S) `reference_evidence_id`; each binding must match its slot, candidate, fingerprint, section sequence, and `Form/Flow`. Keep all 10 `Harmony` fields distinct and newly composed from their references' high-level models. Before binding, route exact language to TrackSpec, vocal boundary and high-note policy to `Vocal`, climax and assigned hook prominence to `Form/Flow`, and arrangement range to `Production/Mix`; repeat playlist-wide rules in the contract and affected TrackSpecs. A random hook level uses the workflow's recorded seed and balanced shuffled bag, never a new structure.

## TrackSpec Schema

Use UTF-8 JSON with exactly these required top-level keys:

    {
      "title": "Window Light",
      "language": "en",
      "target_duration_seconds": 210,
      "bpm": 96,
      "metrical_pulses_per_bar": 4,
      "sections": [
        {"tag": "Intro", "bars": 8, "vocal": false},
        {"tag": "Verse", "bars": 16, "vocal": true},
        {"tag": "Chorus", "bars": 8, "vocal": true},
        {"tag": "Verse", "bars": 16, "vocal": true},
        {"tag": "Chorus", "bars": 8, "vocal": true},
        {"tag": "Bridge", "bars": 8, "vocal": true},
        {"tag": "Chorus", "bars": 8, "vocal": true},
        {"tag": "Outro", "bars": 12, "vocal": false}
      ],
      "prompt_fields": {
        "Style": "Modern indie soul with soft jazz-pop color",
        "Feel": "Warm window-seat reading; calm forward motion",
        "Tempo/Groove": "96 BPM, 4/4; relaxed straight-eighth pocket",
        "Vocal": "One clear alto A3-D5; close natural English; D5 ceiling, one controlled peak",
        "Instrumentation": "Rhodes lead, muted guitar, round bass, compact drums",
        "Harmony": "Gmaj7-Em7-Am7-D9; gentle plagal color on returns",
        "Form/Flow": "Quiet entry, two verse-chorus rises, bridge, harmonic-color peak, soft exit",
        "Production/Mix": "Moderate arrangement dynamic range, close lead, short room, centered lows"
      },
      "exclusion_prompt": "screamed vocals, trap hats, brickwall limiting"
    }

Use language values `en`, `ko`, or `ja`. Give every section exactly `tag`, `bars`, and `vocal`. Include every ordered Basic Prompt field in `prompt_fields`, once, with a nonempty single-line value. Keep `exclusion_prompt` as a string, including an empty string when no trait is absolutely forbidden. Keep the PlaylistSpec, catalog, and draft together when a workspace is available. For a standalone single-track request, keep the TrackSpec beside the draft.

## Emit Three Exact Code Blocks

Use the following shape exactly:

    **기본프롬프트**
    ```text
    <compiled Basic Prompt>
    ```

    **절대불가프롬프트**
    ```text
    <comma-separated absolute exclusions>
    ```

    ### <title>

    **가사**
    ```text
    <supported tags and complete lyrics only>
    ```

Use each bold field heading once and in that order. Open and close every block with three grave accents and the `text` info string. Emit exactly three fenced blocks. Put the title only in the level-three heading between the second block and the Lyrics heading. Never put a title line inside a code block.

## Compile The Basic Prompt

Join the eight `prompt_fields` in this exact order as `Field: value`, separated by one space:

1. Style: region or market, era, central genre, and adjacent influence
2. Feel: use case, emotion, arousal, brightness, and motion
3. Tempo/Groove: BPM, meter or pulse, pocket, and rhythmic feel
4. Vocal: lead identity, range, vocal upper boundary, high-note policy, timbre, phrasing, pronunciation, emotion, and naturalness
5. Instrumentation: instrument roles, register, texture, and arrangement behavior
6. Harmony: newly designed section-level progressions, cadence, color, and bass motion
7. Form/Flow: supported sequence, entry, build, peak, return, and ending in prose
8. Production/Mix: performance, arrangement dynamic range, mic distance, space, stereo, tone, and processing

Target 800 Unicode characters or fewer. Permit up to 100 extra characters when needed, with 900 as the hard maximum. Field names and values must match TrackSpec verbatim. Keep artist names, song titles, citations, lyric lines, absolute prohibitions, and bracketed structural tags out of this block. Use only positive audible direction. Structure tags belong only in Lyrics.

## Compile The Absolute Exclusion Prompt

Use a comma-separated list of only traits whose presence would make the result unusable. Keep it at 100 Unicode characters or fewer. Do not duplicate a prohibition in `prompt_fields`. Leave the fenced block empty when there is no absolute prohibition.

## Compile The Outside Title And Lyrics Block

Render the exact TrackSpec title as `### <title>` outside the code blocks. Inside the Lyrics block, write only the exact ordered TrackSpec tags and complete lyrics in the selected language.

Supported functional tags are:

`Intro, Verse, Pre-Chorus, Chorus, Bridge, Outro, Hook, Refrain, Break, Drop, Coda`.

Map musical function to the closest supported tag and preserve TrackSpec order. Write every repeated passage in full; never use placeholder text, `x2`, or repeat instructions. Supply performable text for every section marked `vocal: true`. Leave a `vocal: false` section free of lyric lines.

The bar plan must calculate to 180-240 seconds. Prefer 195-225 seconds to absorb generation variance. The validator checks conservative lyric-line and language-unit density as duration readiness; only rendered audio can prove actual runtime.

## Validate Atomically

For playlist track `N`, validate the entire bound playlist and its compiled output:

    python3 scripts/validate_playlist_spec.py playlist-spec.json --catalog structure-catalog.json
    python3 scripts/validate_track_output.py draft.md --playlist playlist-spec.json --catalog structure-catalog.json --track N

For an explicit single-track request only:

    python3 scripts/validate_track_output.py draft.md --spec track-spec.json

`PLAN PASS` requires:

- exactly the three requested fenced fields in order, with the title outside them
- catalog, slot, fingerprint, section-sequence, and Form/Flow binding
- prompt field order, exact bound-TrackSpec traceability, and character caps
- a matching absolute-exclusion field
- matching title, language, tags, vocal flags, and complete repeated lyrics
- a 180-240 second target and bar-plan calculation
- a plausible lyric load for the planned vocal bars

On failure, update TrackSpec or regenerate the complete dependent block, then validate the entire file again. Limit internal repair to three attempts and report any remaining deterministic error.

## Deliver Clear Status

Use `PLAN PASS` for deterministic text validation. Use `draft-validated` only after a fresh review bound by `lyrics_sha256` passes `validate_lyric_review.py`. Use render labels only after their audio checks pass.
