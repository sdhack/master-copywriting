# Evidence-based Voice Profile

Build account voice from observable samples, never from an invented persona.

## Evidence Minimum

- Recommended: 10-20 representative, recent samples.
- Record source file or URL, date, sample count, platform, and exclusions.
- Fewer samples may support low-confidence observations only.
- No samples: return `missing evidence`; use platform-native neutral voice.

## Profile Fields

For every trait record `value`, `evidence`, and `confidence`:

- information order
- sentence rhythm and length variation
- judgment style and degree of certainty
- stable vocabulary and avoided vocabulary
- openings, transitions, and endings
- authentic quirks supported by repeated evidence
- forbidden or invented traits

Do not infer biography, private experience, demographic identity, or stable beliefs from writing style alone.

## Runtime Use

Apply only high-confidence traits globally. Use medium-confidence traits sparingly. Ignore low-confidence traits during generation. H1 and H2 preserve authentic irregularity; they must not turn the profile into repeated catchphrases.
