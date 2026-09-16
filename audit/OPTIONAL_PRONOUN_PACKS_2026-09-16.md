# SDS 3.13.4 — Optional Romance Pronoun Packs

Date: 2026-09-16

This record documents two optional Vietnamese pronoun overlays built on top of the audited Name + Item + Gender Lock Build 1. They are mutually exclusive choices and are not replacements for the canonical name/gender audit.

## Option A — Male Romance

Target romanceable male NPCs:

- Lucas
- Pelette
- Uriel
- Sariel
- Lane
- Rane
- Hovsep

Policy:

- Early / 0–6 heart dialogue: NPC self = `tôi`; male Farmer = `cậu`; female Farmer = `cô`.
- Deep / 8–10 heart, dating/spouse/marriage dialogue: NPC self = `anh`; Farmer = `em`.
- Player response labels, narration, third-person phrases (`cậu ấy`, `cậu ta`, etc.), friend nouns, and known Lane/Rane sibling-only clauses are protected from mechanical rewriting.
- Siren is excluded because Siren intentionally changes gender by route/form.

QA:

- CP key count: 24,827 / 24,827
- DLL key count: 2,419 / 2,419
- CP changed keys: 5,166
- DLL changed keys: 280
- Dialogue/control-token mismatches: 0
- Nested/invalid inline gender tokens: 0
- Session ZIP: `SDS-3.13.4-Optional-Pronouns-Male-Romance.zip`
- SHA256: `f6274c992095c7a1b357104c839c03240fca4b2cd44d793d090d485a5cc45b3e`

## Option B — Female Romance

Target romanceable female NPCs:

- Regla
- Luoli
- Maria

Policy:

- Early / 0–6 heart dialogue: NPC self = `tôi`; male Farmer = `anh`; female Farmer = `chị`.
- Deep / 8–10 heart, dating/spouse/marriage dialogue: NPC self = `em`; male Farmer = `anh`; female Farmer = `chị`.
- Player response labels, narration, third-person phrases and friend nouns are protected from mechanical rewriting.
- Siren is excluded because Siren intentionally changes gender by route/form.

QA:

- CP key count: 24,827 / 24,827
- DLL key count: 2,419 / 2,419
- CP changed keys: 351
- DLL changed keys: 32
- Dialogue/control-token mismatches: 0
- Nested/invalid inline gender tokens: 0
- Session ZIP: `SDS-3.13.4-Optional-Pronouns-Female-Romance.zip`
- SHA256: `e603013988900934e2d2536c0b49bae21bb89149b9c659372f8141c03b5c5de6`

## Combined selector bundle

- `SDS-3.13.4-Optional-Pronoun-Packs-A-B.zip`
- SHA256: `7718696f4fc681e6845fb3f81a9f1f80670c4e7e3ccb4e006a081631623ebddd`
- Contains `OPTION-A-NAM` and `OPTION-B-NU` folders.
- Users must install only one option at a time because both overlays replace the same two `vi.json` files.

## Technical notes

- Both packs preserve the audited canonical proper names/items and Gender Lock foundation.
- Existing inline player-gender syntax from the translation is reused, with `${cậu^cô}$` for Option A early dialogue and `${anh^chị}$` for Option B.
- `Siren` must remain route-aware and must never be globally forced into either binary pack.
- The large repository release `vi.json` blobs are not rebuilt by this documentation commit. The session ZIPs are the validated optional artifacts.
