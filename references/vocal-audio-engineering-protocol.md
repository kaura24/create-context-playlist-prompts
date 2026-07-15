# Vocal Naturalness And Audio Engineering Protocol

Use this protocol when designing vocals and mixes, when the user says a voice sounds artificial or "too AI," and during every A/B/C listening cycle. A prompt can steer generation but cannot guarantee removal of synthesis artifacts; diagnose audible symptoms and learn from renders instead of promising a deterministic fix.

## Separate The Audible Layers

- `Vocal identity`: range, register balance, timbre, formant character, and identity stability
- `Performance`: breath placement, onset, pitch movement, vibrato, melisma, dynamics, and phrase endings
- `Language delivery`: pronunciation, consonant clarity, vowel continuity, syllabic stress, and timing
- `Capture`: mic distance, dryness, room reflections, proximity, and noise texture
- `Mix`: compression, de-essing, saturation, EQ balance, reverb/delay, stereo placement, and lead/background separation
- `Generation artifacts`: metallic resonance, formant wobble, abrupt timbre changes, smeared consonants, phasey doubling, clipped breaths, or unnaturally perfect pitch steps

Do not use `AI-like voice` as the diagnosis. Record the specific audible symptom and desired opposite. Mark anything that cannot be judged from the available audio as unconfirmed.

## Build The Diagnostic Table

Present this table in Korean when a render needs diagnosis:

`Layer | Heard symptom | Desired opposite | Evidence/uncertainty | Positive Main Prompt direction | Exclusion candidate | A/B/C test axis`

Do not assume every problem belongs in the prompt. Separate composition, vocal performance, capture, mix, and model artifact causes before revising.

## Define The Vocal And Engineering Contract

Approve these values for the playlist and update them from listening evidence:

`Vocal identity | Performance naturalness | Korean/Japanese/English delivery | Mic/room | Dynamics processing | Tonal balance | Stereo position | Accepted texture | Rejected artifacts`

Keep identity-defining values common across tracks. Allow track-specific engineering variation only inside the Playlist sound contract and the current track's approved role.

## Write Positive Main Prompt Directions

Use concise, audible, engineering-oriented language. Select only relevant traits, such as:

- Stable single-lead identity and register
- Conversational or legato phrasing with phrase-level breath placement
- Restrained or specified vibrato and melisma
- Clear consonants, continuous vowels, and natural syllabic stress
- Close or moderate mic distance and an explicit room size
- Controlled compression that preserves phrase dynamics
- Centered mono-compatible lead with defined background-vocal scope
- Gentle saturation, controlled sibilance, soft transients, or another approved tonal target

Do not stack vague terms such as `organic`, `human`, `realistic`, and `natural` without stating the audible behavior they mean. Do not put bracketed Lyrics tags in Main Prompt A/B/C.

## Use A/B/C As A Controlled Engineering Test

Keep title, lyrics, Lyrics tag sequence, lead-vocal identity, language, central genre, and Exclusion Prompt fixed. Keep form development, flow, harmony, feel, and instrumentation similar rather than identical within their approved envelopes. Similarity makes a field eligible for bounded testing; it does not require changing every field. Keep non-test-axis fields semantically at the A baseline. Choose one unresolved engineering or vocal-performance axis; use two only when they are causally linked.

- `A`: direct compilation of the approved track row and active Calibration Lock, with no comparison-axis deviation
- `B`: one bounded alternative on the test axis
- `C`: the opposite or intermediate bounded alternative

State the expected audible difference without claiming certainty. After listening, record the chosen prompt, actual audible result, failed descriptors, successful descriptors, and the resulting Calibration Lock update.

## Reserve Exclusion Prompt For Critical Artifacts

Use only the highest-impact absolute prohibitions that fit the 100-character cap. Prefer specific symptoms such as `metallic vocal tone`, `formant wobble`, `smeared consonants`, or `stacked lead vocals` over the vague phrase `AI voice`. Keep positive replacements in Main Prompt A/B/C and do not duplicate the same prohibition there.

## Feature-Aware Fallback

If prompt calibration repeatedly fails and the user has access to a suitable Suno feature, explain the option separately from the prompt:

- Suno Voices can use an owned voice recording; official guidance recommends a clean acapella in a neutral room and notes that higher Audio Influence can improve resemblance.
- Personas can preserve vocal and style characteristics from an approved Suno song.

Do not assume feature availability, ownership rights, model version, or slider settings. Record them as runtime variables rather than embedding them as musical facts in the Main Prompt.

## Final Gate

- Every naturalness instruction names an audible trait.
- A/B/C differ only on declared vocal or engineering axes.
- Lyrics, tag sequence, central genre, vocal identity, and exclusions stay fixed; any declared harmony, form-development, flow, or engineering variant stays inside its approved envelope.
- Main Prompts use positive directions; Exclusion Prompt holds only critical artifacts.
- Listening feedback updates the Calibration Lock only with its recorded scope and expiry.

## Official Sources

- [Music Glossary for Suno](https://help.suno.com/en/articles/9010177)
- [Create in V4.5: Detailed Style Instructions](https://help.suno.com/en/articles/5782849)
- [Voices: Use Your Voice in Suno](https://help.suno.com/en/articles/11362369)
- [What are Personas?](https://help.suno.com/en/articles/3484161)
