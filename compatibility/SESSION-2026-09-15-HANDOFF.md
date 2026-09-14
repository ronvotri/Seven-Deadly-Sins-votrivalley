# SESSION HANDOFF — 2026-09-15

> Source of truth for the next chat. Read this before touching translation or compatibility work.

## 1. SDS Vietnamese localization

Seven Deadly Sins source version: **3.13.4**.

Localization remains complete and clean:

- CP: **24,827 / 24,827**
- DLL: **2,419 / 2,419**
- CP canonical commit: `2ca310f`
- DLL canonical commit: `c2e0461693e423785a6dc4ea44eb5fc430b84949`
- canonical localization-only archive: `dist/Seven-Deadly-Sins-3.13.4-Vietnamese-Localization.zip`
- release commit: `cac241011ff8e0eb15d8902ed94b06e78006bfa7`

Do **not** restart translation unless the source mod updates or the user reports a concrete in-game localization bug.

### Session-local ZIPs produced

The user re-uploaded the canonical localization ZIP and the Vietnamese visual hotfix, and they were repackaged into:

1. `SDS-3.13.4-Vietnamese-Localization.zip`
   - localization only
   - SHA256: `eebdb40d5343d5c6809b7a5c7e199d03a31cd0ee3f2a2d386e62a8e8e044adce`

2. `SDS-3.13.4-Vietnamese-Localization-Visual-Hotfix.zip`
   - CP + DLL Vietnamese localization
   - plus the 3 Vietnamese statement images
   - SHA256: `1b36c1bb14d6cac1c3726acbe04862d5016f4dc2f2afcf870db0dad46acc1236`

The second package is the user's preferred all-in-one localization package for now.

## 2. Visual localization

The three baked Chinese statement images were identified outside JSON localization:

- `[CP] Seven Deadly Sins/Maps/CG/SDS.statement1.png`
- `[CP] Seven Deadly Sins/Maps/CG/SDS.statement2.png`
- `[CP] Seven Deadly Sins/Maps/CG/SDS.statement3.png`

User status at session end: **temporarily OK / accepted**.

The merged visual package above contains exactly these PNG replacements plus the Vietnamese JSON localization. It does not include map, warp, minimap, or gameplay edits.

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

1. Read this file, root `HANDOFF.md`, and `CHECKPOINT.json` first.
2. Treat SDS Vietnamese text localization as complete.
3. Treat portraits and the three Vietnamese statement images as temporarily solved/accepted.
4. Use native SVE/East Scarp bridge routing, not DirectRoute TEST2.
5. If the user asks for minimap compatibility, start from the **LITE** pack, not TEST1-TEST8.
6. Do not attempt another Shearwater marker fix unless the user explicitly wants to reopen that research.
7. If a downloadable LITE ZIP is needed in a fresh runtime, rebuild it from `build_npcmap_compat_lite.py`.

## 9. Current priority

There is no mandatory open bug at session end. The project is in a stable handoff state.

Likely next work should come from a new user request, rather than continuing the abandoned minimap investigation automatically.
