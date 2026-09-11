# HANDOFF - Seven Deadly Sins 3.13.4

> **Vietnamese localization is complete, clean, packaged and release-ready. Do not resume translation unless an in-game localization bug or a new source version appears.**

## Localization status

- CP: **24,827 / 24,827**, clean audit, canonical commit `2ca310f`
- DLL: **2,419 / 2,419**, clean audit, canonical commit `c2e0461693e423785a6dc4ea44eb5fc430b84949`
- Release commit: `cac241011ff8e0eb15d8902ed94b06e78006bfa7`
- Release archive: `dist/Seven-Deadly-Sins-3.13.4-Vietnamese-Localization.zip`

---

# COMPATIBILITY RESEARCH

Primary source of truth:

`compatibility/SDS-EastScarp-SVE-RESEARCH.md`

Session-closeout handoff for the next chat/session:

`compatibility/SESSION-2026-09-11-HANDOFF.md`

Current session handoff commit:

`85b23342d6155da49a01a15beb6779df6e037ffa`

Runtime validation matrix:

`compatibility/RUNTIME-VALIDATION-CHECKLIST.md`

Runtime checklist commit:

`3bc0be9f50b01f9586f715ac16068822ab344577`

Latest completed map-research commit:

`58df2ebb03fa4f20c7a97f24d2c27e4bd51e3ce7`

Current runtime-phase checkpoint commit:

`4e395b536d4ce4c40b5227cbd4187da62ed60733`

Versions audited:

- Seven Deadly Sins **3.13.4**
- East Scarp **3.0.9**
- SVE-aware routing checked against current upstream SVE Town layout used in the completed map audit

## Exact sources

### SDS

Exact SDS 3.13.4 map source was extracted from Nexus file `178657` through the SMAPI dataset:

- run `34609160529`
- artifact ID `10267372515`

### East Scarp

User supplied full `East Scarp.rar`.

Exact East Scarp Core 3.0.9 files were successfully extracted locally, including `content.json`, `SVE.json`, `Town_ES.tmx`, `ScarpCrossing_SVE.tmx`, and `ES_ShearwaterBridgeStrip.tmx`.

A separate SMAPI dataset extraction attempt, run `34614235814`, failed only because the dataset export did not expose the current unpacked 3.0.9 core. This does not invalidate the direct archive analysis.

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

Exact route:

- SVE Town outgoing warp: X119, Y72-76 -> `Custom_ShearwaterBridge`
- East Scarp bridge return: -> Town `118,72`

SDS SVE main patch covers `X110 Y0 W63 H116` at Priority Late, but exact tile inspection shows:

- Town 118,72 is walkable
- Town 119,72-76 is walkable in all three SDS main variants
- those warp tiles contain no Buildings/Buildings2/Buildings7 blockers
- a continuous walkable route exists from the warp strip back into Town in all three variants
- SDS does not target `Custom_ShearwaterBridge` or any East Scarp location
- SDS main patch does not replace SVE's Town Warp map-property key

Other exact East Scarp SVE-aware edits also do not geometrically overlap SDS:

- East Scarp Town quest/garden: around X59-68, Y13-20
- East Scarp Mountain: X86 Y35 W9 H6

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

# RUNTIME VALIDATION FRAMEWORK

The runtime phase is now prepared in:

`compatibility/RUNTIME-VALIDATION-CHECKLIST.md`

It defines PASS/FAIL checks for:

- clean SMAPI launch and dependency/load errors;
- Town -> Custom_ShearwaterBridge -> EastScarp_Village;
- East Scarp -> Custom_ShearwaterBridge -> Town 118,72;
- SDS Avalia Forest access;
- Pelipper compatibility packs;
- Ridgeside Village sanity travel;
- NPC schedules/pathfinding;
- festival maps and placements;
- runtime failure classification and minimal-patch policy.

No runtime result has been claimed yet. A fresh full SMAPI log from the intended modpack is still required before diagnosing or patching a runtime problem.

---

# EXACT NEXT ACTION

**Read `compatibility/SESSION-2026-09-11-HANDOFF.md` and `compatibility/RUNTIME-VALIDATION-CHECKLIST.md` first in the next work session.**

Do not restart map research from zero and do not resume localization.

Next phase is **runtime validation**:

1. launch the intended full modpack and load a save;
2. exercise Town -> Shearwater Bridge -> East Scarp and return;
3. capture a fresh complete SMAPI log from that same run;
4. inspect dependency, Content Patcher, map, warp, schedule, festival and load-order issues;
5. verify SDS Avalia Forest access still works;
6. sanity-test RSV and installed Pelipper integrations;
7. only build a compatibility patch if a concrete reproducible runtime issue remains.

If a no-SVE setup is specifically requested later, build a dedicated reroute compatibility mod because that case is already proven incompatible.

## Persistence rule

Every confirmed finding, runtime fix or compatibility patch must be committed to GitHub before being called complete. End each future session by updating `CHECKPOINT.json`, `HANDOFF.md`, and the compatibility research/session handoff as appropriate.
