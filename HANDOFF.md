# HANDOFF - Seven Deadly Sins 3.13.4

> **Vietnamese localization is complete, clean, packaged and release-ready. Do not resume translation unless an in-game localization bug or a new source version appears.**

## Localization status

- CP: **24,827 / 24,827**, clean audit, canonical commit `2ca310f`
- DLL: **2,419 / 2,419**, clean audit, canonical commit `c2e0461693e423785a6dc4ea44eb5fc430b84949`
- Release commit: `cac241011ff8e0eb15d8902ed94b06e78006bfa7`
- Release archive: `dist/Seven-Deadly-Sins-3.13.4-Vietnamese-Localization.zip`

---

# COMPATIBILITY RESEARCH

Source of truth:

`compatibility/SDS-EastScarp-SVE-RESEARCH.md`

Latest research commit:

`58df2ebb03fa4f20c7a97f24d2c27e4bd51e3ce7`

Versions audited:

- Seven Deadly Sins **3.13.4**
- East Scarp **3.0.9**
- SVE-aware routing checked against current upstream SVE Town layout

## Exact sources

### SDS

Exact SDS 3.13.4 map source was extracted from Nexus file `178657` through the SMAPI dataset:

- run `34609160529`
- artifact ID `10267372515`

### East Scarp

User supplied full `East Scarp.rar`.

Exact East Scarp Core 3.0.9 files were successfully extracted locally with libarchive, including `content.json`, `SVE.json`, `Town_ES.tmx`, `ScarpCrossing_SVE.tmx`, and `ES_ShearwaterBridgeStrip.tmx`.

A separate SMAPI dataset extraction attempt, run `34614235814`, failed only because the dataset export did not expose the current unpacked 3.0.9 core. This failure does not invalidate the local exact archive analysis.

---

# FINAL MAP-LEVEL CLASSIFICATION

## SDS + East Scarp WITHOUT SVE

### 🔴 CONFIRMED HARD MAP CONFLICT

East Scarp patches:

`Maps/Town X109 Y63 W21 H14`

SDS without SVE loads the entire `Maps/SDS.Town.tmx`.

Within the exact East Scarp rectangle, SDS has:

- Back: 294 / 294 occupied
- Buildings: 222 / 294
- Front: 111 / 294
- AlwaysFront: 112 / 294

Therefore a compatibility/reroute patch is required if running SDS + East Scarp without SVE.

## SDS + East Scarp + SVE

### 🟢 MAP-LEVEL COMPATIBLE, RUNTIME VALIDATION RECOMMENDED

East Scarp disables `Town_ES.tmx` when SVE exists and instead routes through:

`Town -> Custom_ShearwaterBridge -> EastScarp_Village`

Exact East Scarp 3.0.9 SVE route:

- SVE Town outgoing warp: X119, Y72-76 -> `Custom_ShearwaterBridge`
- East Scarp bridge return: -> Town `118,72`

SDS SVE main patch covers `X110 Y0 W63 H116` at Priority Late, but exact tile inspection shows:

- Town 118,72 is walkable
- Town 119,72-76 is walkable in all three SDS main variants
- those warp tiles contain no Buildings/Buildings2/Buildings7 blockers
- a continuous walkable route exists from the warp strip back to the western edge of the SDS main patch in all three variants
- SDS does not target `Custom_ShearwaterBridge` or any East Scarp location
- SDS main patch doesn't replace SVE's Town Warp map-property key

Other exact East Scarp SVE-aware edits also do not geometrically overlap SDS:

- East Scarp Town quest/garden: around X59-68, Y13-20
- East Scarp Mountain: X86 Y35 W9 H6
- SDS Town/Mountain patches are elsewhere for those areas

Therefore do **not** make a pre-emptive SDS/East Scarp map patch for the SVE setup. Test in game first.

---

# Practical intended modpack

User is considering:

- SDS 3.13.4
- SVE
- East Scarp 3.0.9
- Ridgeside Village
- Pelipper Town
- PelipperTown.SVE
- PelipperTown.EastScarp
- PelipperTown.RidgesideVillage
- PelipperTown.StarCrossed when StarCrossed is installed

Pelipper optional files only integrate Pelipper with those expansions. They are not SDS compatibility patches.

---

# EXACT NEXT ACTION

Do not restart map research from zero and do not resume localization.

Next work is **runtime validation**:

1. install intended modpack;
2. launch via SMAPI and capture log;
3. verify Town -> Shearwater Bridge -> East Scarp both directions;
4. verify SDS Avalia Forest warp still works;
5. test major festivals and NPC schedules;
6. inspect any Content Patcher conflict/warning in the SMAPI log;
7. only build a compatibility patch if a concrete reproducible issue remains.

If a no-SVE setup is specifically requested later, build a dedicated reroute compatibility mod because that case is already proven incompatible.

## Persistence rule

Every confirmed finding or compatibility patch must be committed to GitHub before being called complete, and CHECKPOINT/HANDOFF should be updated at session end.
