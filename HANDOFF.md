# HANDOFF - Seven Deadly Sins 3.13.4

> **Vietnamese text localization is complete. A proper-name/item consistency audit was completed on 2026-09-15. Two mutually exclusive optional romance-pronoun overlays were built on 2026-09-16. Current stable state is audited localization + optional pronoun pack + optional visual hotfix + an optional Town-only NPC Map Locations LITE patch. Do not restart translation or deep minimap research automatically.**

## Read first in the next chat

`compatibility/SESSION-2026-09-15-HANDOFF.md`

Then:

`CHECKPOINT.json`

Then:

`audit/NAME_ITEM_AUDIT_2026-09-15.md`

Then:

`audit/OPTIONAL_PRONOUN_PACKS_2026-09-16.md`

Historical compatibility research remains under `compatibility/`.

---

## Localization status

- CP: **24,827 / 24,827**, clean audit, original canonical commit `2ca310f`
- DLL: **2,419 / 2,419**, clean audit, original canonical commit `c2e0461693e423785a6dc4ea44eb5fc430b84949`
- original localization-only archive: `dist/Seven-Deadly-Sins-3.13.4-Vietnamese-Localization.zip`
- original release commit: `cac241011ff8e0eb15d8902ed94b06e78006bfa7`

### 2026-09-15 proper-name / item consistency audit

Triggered by a concrete report that character names and item naming were inconsistent in the current Vietnamese release.

The two user-supplied Vietnamese files were verified byte-for-byte against the repository release before repair, so this audit was performed on the current release state rather than an older copy.

Completed audit results:

- CP changed keys: **1,262**
- DLL changed keys: **195**
- CP key count preserved: **24,827**
- DLL key count preserved: **2,419**
- dialogue/event control-token mismatches: **0**
- known bad name aliases remaining: **0**
- matched English display-name keys audited: **390**
- outfit sets standardized: **9**

Canonical English proper-name spellings locked by this audit include:

`Sariel`, `Lane`, `Rane`, `Pelette`, `Garnet`, `Regla`, `Teresa`, `Theodor`, `Coffey`, `Xenia`, `Siren`, `Lucas`, `Five Songs`.

Do not reintroduce old/incorrect forms when they represent those characters, including:

`Shirai`, `Baibai`, `Garrett`, `Rigela`, `Theresa`, `Theodore`, `Kofi`, `Zinnia`, `Tiểu Se`, `Tiểu Sai`, `Xiao Sai`, `Bạch Tỉnh`, `Ryan`, `Rhein`, `Pellet`, `Fivesongs`.

The audit also fixed Lane/Rane doll and ice-cream naming/descriptions, Sariel doll naming, several wrong-character references, and inconsistent paired outfit set names.

Audit record:

`audit/NAME_ITEM_AUDIT_2026-09-15.md`

Audit record commit:

`30db501c10048243cbc8187ac07fae0659b8dcd2`

Audited file checksums:

- CP `vi.json`: `42bc9b5b9f61a09c00416cdb3cae80e41f8346015ed46361f8ca87784e3d8f18`
- DLL `vi.json`: `fd09cbb6e32377267c417184c1576e0bee56aa0e9c33d3481758da6eed538a65`
- session ZIP `SDS-3.13.4-Vietnamese-Name-Item-Audit-Fix.zip`: `7554385561307026b4674fbf01b4fe1640bad1fd4f1af3cc45e1616b6f264b54`

**Important repo note:** the large release `vi.json` blobs in `release/` have not yet been rebuilt from the audited session artifact. Until an explicit release rebuild is performed, use the audited session ZIP/checksums above as the preferred text-localization state and never restore old aliases from the pre-audit release blobs.

### 2026-09-16 optional romance-pronoun packs

Built on top of the audited Name + Item + Gender Lock foundation. These are **mutually exclusive optional overlays** and users install only one at a time.

**Option A — Male Romance**

Targets: `Lucas`, `Pelette`, `Uriel`, `Sariel`, `Lane`, `Rane`, `Hovsep`.

- early / 0–6 hearts: NPC `tôi`; male Farmer `cậu`; female Farmer `cô`
- deep / 8–10 hearts + dating/spouse/marriage: NPC `anh`; Farmer `em`
- CP changed: **5,166**
- DLL changed: **280**
- control-token mismatches: **0**
- ZIP: `SDS-3.13.4-Optional-Pronouns-Male-Romance.zip`
- SHA256: `f6274c992095c7a1b357104c839c03240fca4b2cd44d793d090d485a5cc45b3e`

**Option B — Female Romance**

Targets: `Regla`, `Luoli`, `Maria`.

- early / 0–6 hearts: NPC `tôi`; male Farmer `anh`; female Farmer `chị`
- deep / 8–10 hearts + dating/spouse/marriage: NPC `em`; male Farmer `anh`; female Farmer `chị`
- CP changed: **351**
- DLL changed: **32**
- control-token mismatches: **0**
- ZIP: `SDS-3.13.4-Optional-Pronouns-Female-Romance.zip`
- SHA256: `e603013988900934e2d2536c0b49bae21bb89149b9c659372f8141c03b5c5de6`

Combined selector bundle:

- `SDS-3.13.4-Optional-Pronoun-Packs-A-B.zip`
- SHA256: `7718696f4fc681e6845fb3f81a9f1f80670c4e7e3ccb4e006a081631623ebddd`

Important rules:

- `Siren` is excluded from both binary packs because Siren intentionally changes gender by route/form.
- Preserve narration, player response labels, NPC-to-NPC pronouns, and third-person phrases rather than mechanically rewriting them.
- Continue future editorial QA speaker-by-speaker. Never run a global pronoun search/replace over the entire localization.
- The session ZIPs are the validated optional artifacts; large repository release `vi.json` blobs have not been rebuilt with these overlays.

Audit record:

`audit/OPTIONAL_PRONOUN_PACKS_2026-09-16.md`

Audit commit:

`bbdfdc2a2c98f616bc8ac656f2dea6807ad5df9e`

Do not restart broad translation unless:

1. SDS source version changes, or
2. the user reports a new concrete in-game localization bug, or
3. the user explicitly asks to continue speaker-by-speaker editorial polish.

---

## Visual localization

The baked statement screens are outside the JSON audit:

- `SDS.statement1.png`
- `SDS.statement2.png`
- `SDS.statement3.png`

A merged localization + visual-hotfix ZIP was created in the 2026-09-15 chat.

User status: **temporarily OK / accepted**.

Do not reopen this unless requested.

---

## Portraiture

Verified setup:

`Mods/Portraiture/Portraits/Seven Deadly Sins/`

Active set:

`Seven Deadly Sins`

User status: **temporarily OK / accepted**.

Do not repeat folder/config troubleshooting unless a new portrait issue appears.

---

# SVE + East Scarp route decision

Preferred route:

`main world / railroad <-> Custom_ShearwaterBridge <-> EastScarp_Village`

The old direct route patch:

`compatibility/patches/SDS-SVE-EastScarp-DirectRoute-TEST2/`

is **rejected for normal use** because it produced an asymmetric/bypassing route. Keep it only as historical research.

Do not promote it unless the user explicitly reopens route compatibility.

---

# NPC Map Locations status

NPC Map Locations 3.5.2 uses Stardew 1.6 `Data/WorldMap` / `WorldMapManager.GetPositionData`.

Important runtime findings:

- Town WorldPositions are order-sensitive.
- Custom positions need `MoveEntries` before `Default` when their tile zones overlap Default.
- TEST5 confirmed `VotriValley.SDS_BridgeCorridor` matching at Town `(62,54)`, `(69,53)`, `(74,54)`.
- TEST6 restored the calibrated Town Default runtime pixel area to `X588 Y184 Width180 Height320` instead of SVE's wide `Width388` mapping.
- The user reported the Town side fixed/acceptable afterward.
- `Custom_ShearwaterBridge` continued to report original SVE runtime pixel area `X1000 Y360 Width172 Height40` through later attempts.
- The user explicitly stopped further deep minimap debugging.

## Final practical pack: LITE

Source:

`compatibility/patches/SDS-SVE-NPCMapLocations-Compat-LITE/`

Builder:

`compatibility/patches/build_npcmap_compat_lite.py`

UniqueID:

`VotriValley.SDS.SVE.NPCMapLocations.CompatLite`

LITE keeps only:

- calibrated Town `Default`
- `VotriValley.SDS_BridgeCorridor`
- `VotriValley.SDS_EastTown`
- correct ordering before `Default`

LITE intentionally does **not** touch:

- `Custom_ShearwaterBridge`
- real map layers
- terrain / Buildings
- warps
- East Scarp route
- minimap areas outside Town

Known limitation: Shearwater Bridge marker may remain inaccurate. This is accepted as a visual-only limitation.

Install rule:

1. Remove old NPC Map Locations TEST1 through TEST8.
2. Install only `[CP] SDS-SVE-NPCMapLocations-Compat-LITE` if the user wants the Town minimap improvement.
3. Restart the game fully.

Do **not** hand the user TEST1-TEST8 as the current solution.

---

# Exact next action

There is no mandatory open bug at session end.

When resuming:

1. Read `compatibility/SESSION-2026-09-15-HANDOFF.md`, `CHECKPOINT.json`, `audit/NAME_ITEM_AUDIT_2026-09-15.md`, and `audit/OPTIONAL_PRONOUN_PACKS_2026-09-16.md`.
2. Treat the audited Vietnamese localization as the canonical base and preserve canonical English character spellings.
3. If testing romance phrasing, install exactly one optional pronoun overlay over the audited base.
4. Do not reintroduce pre-audit aliases.
5. Treat portraits and the three visual statement images as accepted for now.
6. Keep the native SVE/East Scarp bridge route.
7. Start any future minimap work from LITE only.
8. If dialogue polish resumes, patch concrete speaker/context cases instead of global pronoun replacement.
9. Do not reopen Shearwater marker research unless the user explicitly asks.

---

## Persistence rule

Every confirmed translation/runtime result and compatibility patch must be committed before being considered complete. Update `CHECKPOINT.json`, this root handoff, and the current session handoff whenever runtime or localization state materially changes.
