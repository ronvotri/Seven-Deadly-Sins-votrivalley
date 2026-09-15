# Seven Deadly Sins 3.13.4 — Vietnamese Name & Item Consistency Audit

Date: 2026-09-15

This audit was triggered by a concrete user report that proper names were being localized/transliterated inconsistently (examples: Sariel, Rane, Pelette).

## Source state

The two Vietnamese files supplied for the audit were verified byte-for-byte against the current repository release files before repair:

- CP base blob: `511450e658424618b727053f350d0079b78ddcc1`
- DLL base blob: `44bbffaae07563ce48d040d970a5e2ff6754b3a9`

English reference supplied by the user: `[CP] Seven Deadly Sins/i18n/default.json` plus `NPCs.txt`, `New craftables.txt`, and `Fish.txt`.
Canonical character spelling is determined from English `*.DisplayName` entries when English supporting docs themselves disagree.

## Confirmed repair scope

- CP changed keys: **1,262**
- DLL changed keys: **195**
- Key counts preserved: **24,827 CP / 2,419 DLL**
- Dialogue/event control-character signature mismatches: **0**
- Known bad aliases remaining: **0**
- English matched display-name keys audited: **390**
- Exact-English duplicate display-name fanout inconsistencies after repair: **0**

Canonical names normalized include:

`Sariel`, `Lane`, `Rane`, `Pelette`, `Garnet`, `Regla`, `Teresa`, `Theodor`, `Coffey`, `Xenia`, `Siren`, `Lucas`, `Five Songs`.

Known wrong/unstable forms removed where they represented character names include:

`Shirai`, `Baibai`, `Garrett`, `Rigela`, `Theresa`, `Theodore`, `Kofi`, `Zinnia`, `Tiểu Se`, `Tiểu Sai`, `Xiao Sai`, `Bạch Tỉnh`, `Ryan`, `Rhein`, `Pellet`, `Fivesongs`.

Important: natural Vietnamese words such as `ra`, song text such as `la la la`, and unrelated item/set names are not blindly replaced.

Additional fixes:

- Lane/Rane dolls and ice-cream dolls: corrected swapped names and descriptions.
- Sariel female/ice-cream doll names standardized.
- Nine outfit top/bottom pairs standardized to one Vietnamese base set name.
- Context corrections include Moore/Sariel, Siren/Hovsep, Pelette and Lane/Rane lines where the Vietnamese file had the wrong proper name.

## Audited output checksums

- CP `vi.json`: `42bc9b5b9f61a09c00416cdb3cae80e41f8346015ed46361f8ca87784e3d8f18`
- DLL `vi.json`: `fd09cbb6e32377267c417184c1576e0bee56aa0e9c33d3481758da6eed538a65`
- Session delivery ZIP `SDS-3.13.4-Vietnamese-Name-Item-Audit-Fix.zip`: `7554385561307026b4674fbf01b4fe1640bad1fd4f1af3cc45e1616b6f264b54`

## Resume rule

Treat this name/item audit as complete. Do not reintroduce the pre-audit aliases. Future translation work should use English canonical `DisplayName` spellings for character names and preserve consistent Vietnamese display names for related items.
