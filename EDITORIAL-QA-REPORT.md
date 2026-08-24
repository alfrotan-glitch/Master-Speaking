# Editorial QA Report — *Master Speaking*

Pass 2 of the specification (2026-08-24). Tool: `book/tools/qa_editorial.py` (block-boundary-aware extraction; pyspellchecker + curated ESL whitelist).

## Method

- Text extracted from the semantic master with spaces guaranteed at every block boundary (list items, table cells never fuse words).
- Spellcheck with unfolding of contractions (shouldn’t → should) and possessives (Acho’s → Acho); hyphenated compounds accepted and enumerated; pronunciation lines (IPA /stress respellings) exempt by design — 167 lines.
- Duplicated words, double spaces (raw text nodes), straight quotes/apostrophes, space-before-punctuation.

## Results

- Unknown words: **0**
- Duplicated words: **0**
- Double spaces: **0** · straight quotes: **0** · straight apostrophes: **0** · space-before-punctuation: **0**
- Hyphenated compounds accepted (43 types, all legitimate ESL terms: long-term, non-native, open-minded, self-regulation, machine-dependent…).

## Editorial corrections applied during the project

- 50 logged changes in `CHANGELOG.md`, each with ORIGINAL / CORRECTION / REASON / CONFIDENCE.
- Notable classes: duplicated “Before You Read” blocks removed (8×); jammed MCQ options split (e.g. “excitementb.” artefacts); “quad” → “quote” (U5); “Team AAgree” → “Team A: Agree”; “on-going” → “ongoing”; one straight apostrophe restored as ’ ; activity renumbering (Activity 1/1/2 → 1/2/3); lettered subsection sequences repaired (A. True or False).
- Preserved by decision: author’s voice, stress respellings (fi NAN cial), intentional respellings (turnitoff, pickitup, theez), 
British/American variants quoted from source.

## Known content carries (documented, not “fixed”)

- U5 vocabulary-activation items missing in the source document.
- U8 mismatched T/F instruction (item 2593) dropped.
