# HANDOFF - Seven Deadly Sins 3.13.4

> **Vietnamese text localization is complete. Current stable state is localization + optional visual hotfix + an optional Town-only NPC Map Locations LITE patch. Do not restart translation or deep minimap research automatically.**

## Read first in the next chat

`compatibility/SESSION-2026-09-15-HANDOFF.md`

Then:

`CHECKPOINT.json`

Historical compatibility research remains under `compatibility/`.

---

## Localization status

- CP: **24,827 / 24,827**, clean audit, canonical commit `2ca310f`
- DLL: **2,419 / 2,419**, clean audit, canonical commit `c2e0461693e423785a6dc4ea44eb5fc430b84949`
- canonical localization-only archive: `dist/Seven-Deadly-Sins-3.13.4-Vietnamese-Localization.zip`
- release commit: `cac241011ff8e0eb15d8902ed94b06e78006bfa7`

Do not restart translation unless:

1. SDS source version changes, or
2. the user reports a concrete in-game localization bug.

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

1. Read `compatibility/SESSION-2026-09-15-HANDOFF.md` and `CHECKPOINT.json`.
2. Treat translation as complete.
3. Treat portraits and the three visual statement images as accepted for now.
4. Keep the native SVE/East Scarp bridge route.
5. Start any future minimap work from LITE only.
6. Do not reopen Shearwater marker research unless the user explicitly asks.

---

## Persistence rule

Every confirmed runtime result and compatibility patch must be committed before being considered complete. Update `CHECKPOINT.json`, this root handoff, and the current session handoff whenever runtime state materially changes.
