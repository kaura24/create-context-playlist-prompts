# Suno Style Guide

Use this reference when compiling the final Main Prompt, Exclusion Prompt, and Title And Lyrics. Keep the three fields separate because Suno Custom Mode treats Styles, Advanced options such as Exclude, Lyrics, and Title as distinct inputs.

## Two-Layer Contract

Treat Suno's official published guidance as the `public platform contract`. It defines what each Suno field is for, which musical vocabulary the platform documents, and how Styles, Exclude, Lyrics, and Title are separated.

Treat the user's latest instructions, approved Playlist sound contract, approved 10-track design, and this skill's output limits as the `private project contract`. It defines the desired music, exclusions, structure, language, vocalist, and operating caps.

Compile Main Prompt, Exclusion Prompt, and Title And Lyrics against both contracts. Use the public contract to route information into the correct field. Use the private contract to decide the actual content. When both define a limit, follow the stricter limit. Never let a public example override an approved private requirement.

## Evidence Boundary

The following rules reflect Suno's published guidance.

- Put genre-specific information in the Style field.
- Put lyrics and additional section-level song context in the Lyrics field.
- Use Exclude for unwanted genres, instruments, voice styles, and similar traits.
- Use specific musical vocabulary for tempo, groove, dynamics, structure, instrumentation, texture, vocal technique, harmony, and production.
- Combine compatible genre terms, emotional detail, instruments, and sonic texture when they are part of the approved design.
- Detailed and evocative descriptions can work, but each phrase should still indicate an audible trait.

Suno's accessible official guidance does not publish an exact character maximum for Exclude. Treat `800 characters for Main Prompt` and `100 characters for Exclusion Prompt` as this skill's operating caps, not as claims about Suno's documented platform maximum.

## Main Prompt

Write the Main Prompt primarily in concise English. Use this order unless the approved design requires another priority.

1. `Style:` country or cultural zone, era, market, central genre, and adjacent genre
2. `Feel:` listening use case, emotion, arousal, brightness/darkness, and motion
3. `Tempo/Groove:` BPM, meter when important, pocket, and rhythmic feel
4. `Vocal:` lead range, timbre, power, pronunciation, phrasing, emotional depth, and naturalness target
5. `Instrumentation:` core instruments, track-specific roles, register, and texture
6. `Harmony:` newly designed section-level chord progression, cadence, color, and bass motion
7. `Form/Flow:` approved form and structural trajectory in concise prose, without bracketed Lyrics tags
8. `Production/Mix:` drum performance, hook behavior, dynamics, mic distance, space, stereo image, tonal balance, and processing

Prefer direct musical terms such as `72 BPM`, `syncopated pocket`, `sparse felt piano`, `close dry vocal`, `AABA form`, or `diminuendo coda` only when those terms are supported by the approved evidence. Use evocative wording only when it adds a usable audible direction. Front-load the identity-defining traits and compress secondary details first.

Do not include title, lyric lines, artist or song names, citations, or absolute prohibitions. Do not repeat exclusions, write conflicting descriptors, or use long narrative prose that belongs in the lyrics. Do not use a genre label as a substitute for `Feel`; preserve the approved Playlist sound contract.

Never place `[Verse]`, `[Chorus]`, or any other bracketed section tag in the Main Prompt. Bracketed structural tags belong only in Title And Lyrics.

## Exclusion Prompt

Write a separate comma-separated list of only absolute prohibitions. Prefer bare traits such as `belting, trap hi-hats, key change` over sentences. Prioritize exclusions whose violation would make the result unusable.

Keep the Exclusion Prompt at 100 characters or fewer, including spaces and punctuation. Do not repeat an exclusion in the Main Prompt. If naming an unwanted concept itself causes the model to produce it, omit the concept from both prompts and express only the desired replacement in the Main Prompt.

## Title And Lyrics

Put the title on the first line, then write complete lyrics using the approved single language and exact bracketed Lyrics tag sequence. The official glossary documents `Intro`, `Verse`, `Pre-Chorus`, `Chorus`, `Bridge`, `Outro`, `Hook`, `Refrain`, `Break`, `Drop`, and `Coda`. Add another tag only when current official guidance or a user-provided verified instruction supports it.

Preserve genre-specific form terms in research and design, but map their section functions to Suno-readable tags for the Lyrics field. Never invent a tag, use a poetic scene name as a tag, or convert the source structure into a universal pop sequence merely because `[Verse]` and `[Chorus]` are familiar. If no supported functional mapping exists, stop before final output and resolve the mapping.

Keep genre and production description in the Main Prompt. Put only section-specific performance or development context in the Lyrics field, such as a delayed entry, instrumental break, restrained delivery, or final shortened line. Do not add a universal Verse-Pre-Chorus-Chorus form that was not approved.

## Final Check

- Main Prompt is at most 800 characters, including spaces and punctuation.
- Exclusion Prompt is at most 100 characters, including spaces and punctuation.
- Title And Lyrics uses the approved title, language, evidence-backed form, permitted variation, Structural Flow Contract, and exact bracketed Lyrics tag sequence.
- Main and Exclusion prompts contain no contradiction or duplicated prohibition.
- Every phrase belongs in the Suno field where it will be entered.

## Official Sources

- [Music Glossary for Suno](https://help.suno.com/en/articles/9010177)
- [Create in V4.5: Better Prompts in Lyrics](https://help.suno.com/en/articles/5782977)
- [What's new in V4.5](https://help.suno.com/en/articles/5782593)
- [How do I exclude elements of a song?](https://help.suno.com/en/articles/3161921)
- [Android Create: Custom Mode](https://help.suno.com/en/articles/3726721)
