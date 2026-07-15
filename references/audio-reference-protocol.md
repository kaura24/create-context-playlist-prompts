# Audio Reference Protocol

## Decide The Audio Role First

When the user provides an audio file or generated result, classify it as one of the following.

- `Primary reference`: the center of the playlist identity
- `Supporting reference`: supports only some harmonic, arrangement, or vocal traits
- `Target render`: an approved target output that "should come out feeling like this"
- `Rejected render`: a counterexample used to find failure causes

If the role is clear from the user's wording, do not ask again. Clarify only when it is ambiguous and would materially change the result.

## Separate Evidence Levels

Do not claim you heard a file that you have not actually decoded, listened to, or analyzed. Record one of the following levels.

1. `Metadata only`: filename, format, size, duration, and similar metadata
2. `Measured`: numerical analysis such as BPM estimate, RMS/peak, section energy, or spectrum
3. `Audibly reviewed`: vocal, instrument, groove, and space judgments from actual listening
4. `User-described`: the user's audible description

If analysis tools are unavailable, use the user's description as temporary evidence and do not record technical analysis as completed. Ask permission before any external upload is required.

## Compare Target Renders

When there is a Target render, compare it against the existing design on the following axes.

- Vocal count, identity, range, phrasing, pronunciation, and power
- Emotional depth and vocal lowest note
- Tempo, meter, groove, and drum density
- Structure family, section sequence, intro and first vocal entry, peak placement, and ending behavior
- Instrument roles, layers, and section-level arrangement curve
- Harmonic color and cadence feel
- Hook repetition and melodic density
- Space, vocal front/back placement, reverb, and low-end weight

Mark each item as `match`, `partial match`, `mismatch`, or `cannot judge`. Do not fill unknowns with guesses.

## Turn Failed Results Into Revision Input

For a Rejected render, separate good traits from failure traits. If you cannot determine which expression in the existing Main Prompt or Exclusion Prompt caused the failure, mark it as a cause candidate. Do not add many exclusions at once. Revise in this order.

1. Remove incorrect scope expansions.
2. Remove conflicting positive descriptions.
3. Rewrite the target sound in positive, measurable terms.
4. Keep only absolute prohibitions in the Exclusion Prompt.
5. Rewrite the Main Prompt, Exclusion Prompt, and Title And Lyrics, then check again.

If the Target render provides a new answer, prioritize its observations over the previous failed prompts. However, do not copy the Primary reference's unique melody, hook, riff, exact chord progression, or lyrics.
