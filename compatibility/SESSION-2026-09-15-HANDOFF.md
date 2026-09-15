# SESSION HANDOFF — 2026-09-15

> Source of truth for the next chat. Read this before touching translation or compatibility work.

## 1. SDS Vietnamese localization

Seven Deadly Sins source version: **3.13.4**.

Localization remains complete and clean:

- CP: **24,827 / 24,827**
- DLL: **2,419 / 2,419**
- CP original canonical commit: `2ca310f`
- DLL original canonical commit: `c2e0461693e423785a6dc4ea44eb5fc430b84949`
- original localization-only archive: `dist/Seven-Deadly-Sins-3.13.4-Vietnamese-Localization.zip`
- original release commit: `cac241011ff8e0eb15d8902ed94b06e78006bfa7`

Do **not** restart translation unless the source mod updates or the user reports a concrete in-game localization bug.

### 2026-09-15 proper-name and item consistency audit

A concrete user report identified inconsistent proper names in the current Vietnamese release, including Sariel/Rane/Pelette-related forms. The user supplied the English source and Vietnamese package for a comprehensive audit of character names and item/display names.

Before repair, both supplied Vietnamese `vi.json` files were verified byte-for-byte against the current repository release blobs:

- CP base blob: `511450e658424618b727053f350d0079b78ddcc1`
- DLL base blob: `44bbffaae07563ce48d040d970a5e2ff6754b3a9`

Final audit results:

- CP changed keys: **1,262**
- DLL changed keys: **195**
- CP key count preserved: **24,827**
- DLL key count preserved: **2,419**
- dialogue/event control-token mismatches: **0**
- known bad aliases remaining: **0**
- matched English display-name keys audited: **390**
- duplicate English display-name fanout inconsistencies after repair: **0**
- outfit sets standardized: **9**

Canonical English character spellings locked by the audit include:

`Sariel`, `Lane`, `Rane`, `Pelette`, `Garnet`, `Regla`, `Teresa`, `Theodor`, `Coffey`, `Xenia`, `Siren`, `Lucas`, `Five Songs`.

Do not reintroduce pre-audit forms when they represent those names, including:

`Shirai`, `Baibai`, `Garrett`, `Rigela`, `Theresa`, `Theodore`, `Kofi`, `Zinnia`, `Tiểu Se`, `Tiểu Sai`, `Xiao Sai`, `Bạch Tỉnh`, `Ryan`, `Rhein`, `Pellet`, `Fivesongs`.

The audit also corrected Lane/Rane doll and ice-cream names/descriptions, Sariel doll naming, several wrong-character references, and nine paired outfit set names. Natural Vietnamese words such as `ra`, song text such as `la la la`, and unrelated names were not blindly replaced.

Audit record:

`audit/NAME_ITEM_AUDIT_2026-09-15.md`

Audit record commit:

`30db501c10048243cbc8187ac07fae0659b8dcd2`

Final audited checksums:

- CP `vi.json`: `42bc9b5b9f61a09c00416cdb3cae80e41f8346015ed46361f8ca87784e3d8f18`
- DLL `vi.json`: `fd09cbb6e32377267c417184c1576e0bee56aa0e9c33d3481758da6eed538a65`
- session ZIP `SDS-3.13.4-Vietnamese-Name-Item-Audit-Fix.zip`: `7554385561307026b4674fbf01b4fe1640bad1fd4f1af3cc45e1616b6f264b54`

**Repository note:** the large `release/.../vi.json` files have not yet been rebuilt from this audited artifact. The audited session ZIP is the preferred text-localization state until an explicit release rebuild occurs. Do not use the pre-audit release blobs as a reason to restore old name aliases.

### Earlier session-local ZIPs produced

The user re-uploaded the canonical localization ZIP and the Vietnamese visual hotfix, and they were repackaged into:

1. `SDS-3.13.4-Vietnamese-Localization.zip`
   - localization only
   - SHA256: `eebdb40d5343d5c6809b7a5c7e199d03a31cd0ee3f2a2d386e62a8e8e044adce`

2. `SDS-3.13.4-Vietnamese-Localization-Visual-Hotfix.zip`
   - CP + DLL Vietnamese localization
   - plus the 3 Vietnamese statement images
   - SHA256: `1b36c1bb14d6cac1c3726acbe04862d5016f4dc2f2afcf870db0dad46acc1236`

For text localization, prefer the newer audited name/item ZIP above. The visual statement PNGs remain separately accepted and can be merged again if needed.

## 2. Visual localization

The three baked Chinese statement images were identified outside JSON localization:

- `[CP] Seven Deadly Sins/Maps/CG/SDS.statement1.png`
- `[CP] Seven Deadly Sins/Maps/CG/SDS.statement2.png`
- `[CP] Seven Deadly Sins/Maps/CG/SDS.statement3.png`

User status at session end: **temporarily OK / accepted**.

The earlier merged visual package contains exactly these PNG replacements plus the Vietnamese JSON localization. It does not include map, warp, minimap, or gameplay edits.

## 3. Portraiture

Earlier issue: SDS HD portraits for NPCs such as Raymond/Maria/Edward rendered cropped/huge.

Verified setup:

- portrait folder: `Mods/Portraiture/Portraits/Seven Deadly Sins/`
- active set: `Seven Deadly Sins`
- Portraiture reported the active set loaded

User status at session end: **temporarily OK / accepted**. Do not reopen portrait debugging unless the user reports it again.

## 4. SVE + East Scarp route decision

The previously built direct Town <-> East Scarp route is **rejected** because it created an asymmetric return path and bypassed the natural bridge flow.

Preferred route remains the native chain:

`main world / railroad <-> Custom_ShearwaterBridge <-> EastScarp_Village`

Do not restore or promote `SDS-SVE-EastScarp-DirectRoute-TEST2` unless the user explicitly asks to revisit it.

## 5. NPC Map Locations / minimap research

Target stack:

- SDS 3.13.4
- Stardew Valley Expanded
- East Scarp 3.0.9
- NPC Map Locations 3.5.2 (`Bouhm.NPCMapLocations`)

### Important engine finding

NPC Map Locations 3.5.2 relies on Stardew 1.6 `Data/WorldMap` / `WorldMapManager.GetPositionData` rather than the old MapVectors approach.

SDS changes the visual world map layout without fully matching SVE's `Data/WorldMap`, which explains marker drift.

### Town runtime calibration history

Useful anchors collected:

- `Town (40,26)` — old/default mapping visually OK
- `Town (39,58)` — central Town test point
- `Town (58,53)` — just before bridge corridor
- `Town (62,54)` — corridor
- `Town (69,53)` — corridor
- `Town (74,54)` — corridor
- `Town (79,53)` / `Town (80,53)` — exposed the bad hard X80 seam in earlier tests
- Joja / church area — east-Town calibration judged good

Confirmed runtime behavior:

- custom WorldPositions are order-sensitive
- `MoveEntries` is needed so custom entries are checked before `Default`
- TEST5 successfully matched `VotriValley.SDS_BridgeCorridor` at `(62,54)`, `(69,53)`, `(74,54)`
- TEST6 restored Town Default runtime pixel area from SVE's wide `X588 Y184 Width388 Height320` to calibrated `X588 Y184 Width180 Height320`
- after that, the Town side of the small bridge was reported fixed / acceptable by the user

### Shearwater Bridge unresolved limitation

`Custom_ShearwaterBridge` repeatedly reported original SVE runtime pixel area:

`X1000 Y360 Width172 Height40`

Attempts TEST3 through TEST8 did not produce a reliable runtime change there.

The user explicitly stopped deep minimap debugging and accepted the remaining bridge marker error as a temporary feature limitation.

Do **not** automatically resume Shearwater/minimap research.

## 6. Final practical compatibility pack: LITE

The user later asked for a reduced compatibility pack that is simply usable.

Final source:

`compatibility/patches/SDS-SVE-NPCMapLocations-Compat-LITE/`

Files:

- `manifest.json`
- `content.json`
- `README.md`

Builder:

`compatibility/patches/build_npcmap_compat_lite.py`

UniqueID:

`VotriValley.SDS.SVE.NPCMapLocations.CompatLite`

### LITE scope

Keeps only the validated Town-side fixes:

- calibrated Town `Default`
- `VotriValley.SDS_BridgeCorridor`
- `VotriValley.SDS_EastTown`
- `MoveEntries` before `Default`

Intentionally does **not** touch:

- `Custom_ShearwaterBridge`
- real map layers
- terrain / Buildings
- warp data
- East Scarp route
- minimap areas outside Town

Known limitation:

- Shearwater Bridge marker may remain wrong
- this is visual-only and intentionally accepted

Session-local ZIP:

`SDS-SVE-NPCMapLocations-Compat-LITE.zip`

SHA256:

`484ea5a3f4e8e43146403779b39068f78b223606dc9c792d3c79d8cbfd1114c2`

Install rule:

- remove old NPC Map Locations TEST1 through TEST8
- install only `[CP] SDS-SVE-NPCMapLocations-Compat-LITE`
- restart game fully

## 7. Old test packs

Historical TEST packs remain in the repo for research traceability, but they are **not release candidates**:

- `SDS-SVE-NPCMapLocations-Compat-TEST2` through `TEST8`
- older TEST1 was also experimental
- `SDS-SVE-EastScarp-DirectRoute-TEST2` is rejected for normal use

Do not hand these to the user as the current solution.

## 8. Exact next-session behavior

When the user opens a new chat for this project:

1. Read this file, root `HANDOFF.md`, `CHECKPOINT.json`, and `audit/NAME_ITEM_AUDIT_2026-09-15.md` first.
2. Treat SDS Vietnamese text localization and the name/item consistency audit as complete.
3. Preserve canonical English character spellings and do not reintroduce pre-audit aliases.
4. Treat portraits and the three Vietnamese statement images as temporarily solved/accepted.
5. Use native SVE/East Scarp bridge routing, not DirectRoute TEST2.
6. If the user asks for minimap compatibility, start from the **LITE** pack, not TEST1-TEST8.
7. Do not attempt another Shearwater marker fix unless the user explicitly wants to reopen that research.
8. If a downloadable LITE ZIP is needed in a fresh runtime, rebuild it from `build_npcmap_compat_lite.py`.

## 9. Current priority

There is no mandatory open bug at session end. The project is in a stable handoff state with the audited name/item localization as the preferred text package.

Likely next work should come from a new user request rather than restarting completed localization or the abandoned minimap investigation automatically.
