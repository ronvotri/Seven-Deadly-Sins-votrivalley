# SDS Runtime Compatibility Validation Checklist

> Runtime test plan for the current compatibility phase. This does **not** replace the completed map audit in `SDS-EastScarp-SVE-RESEARCH.md`; it turns the handoff's runtime requirements into a repeatable PASS/FAIL matrix.

## Scope

Primary intended setup:

- Seven Deadly Sins 3.13.4
- Stardew Valley Expanded
- East Scarp 3.0.9
- Ridgeside Village
- Pelipper Town
- `PelipperTown.SVE`
- `PelipperTown.EastScarp`
- `PelipperTown.RidgesideVillage`
- `PelipperTown.StarCrossed` only when StarCrossed is installed

Known static-map classification before runtime testing:

- SDS + East Scarp **without SVE**: confirmed hard map conflict; dedicated reroute patch required.
- SDS + East Scarp + SVE: no hard collision found on the audited Shearwater route; runtime validation required.

Do not create a compatibility patch for the SVE case unless this checklist reproduces a concrete issue.

---

# 1. Test-run identity

Record before interpreting any result:

- Stardew Valley version
- SMAPI version
- Content Patcher version
- SDS version: expected 3.13.4
- SVE version
- East Scarp version: expected 3.0.9 for comparison with the current static audit
- Ridgeside Village version
- Pelipper Town version
- installed Pelipper compatibility packs
- whether StarCrossed is installed
- save used for testing
- in-game season / day / year

If the tested East Scarp or SDS version differs from the audited versions, do not automatically carry forward the old map result as proof for the new version.

---

# 2. Clean launch / SMAPI log

## PASS

- game reaches title screen and save loads;
- no red SMAPI errors caused by SDS, East Scarp, SVE, RSV, Pelipper Town, or their compatibility packs;
- no missing required dependency;
- no duplicate UniqueID;
- no Content Patcher patch rejected because of malformed conditions, missing target assets, invalid map areas, or missing files;
- no repeated exception loop after entering the save.

## FAIL evidence to capture

For every failure, keep:

1. fresh full SMAPI log from the same test run;
2. exact in-game action that triggered it;
3. location name if known;
4. season/day/time;
5. screenshot when the failure is visual or positional.

Do not diagnose from a cropped red line when the complete SMAPI log is available.

---

# 3. East Scarp route through SVE Shearwater Bridge

This is the highest-priority runtime test because the static audit specifically examined this route.

Expected route:

`Town X119,Y72-76 -> Custom_ShearwaterBridge -> EastScarp_Village`

Expected bridge return to Town:

`Town 118,72`

## Test A — Town to East Scarp

1. Enter Pelican Town normally.
2. Walk to the SVE east exit around Town X119,Y72-76.
3. Confirm the warp triggers.
4. Confirm `Custom_ShearwaterBridge` loads without black screen / exception / bad spawn.
5. Continue into East Scarp.
6. Confirm `EastScarp_Village` loads and the player is placed on a usable tile.

### PASS

- all warps trigger;
- no collision wall blocks access to the exit;
- no visual SDS overlay prevents reaching the warp strip;
- no invalid spawn or out-of-bounds placement;
- no SMAPI error on transition.

## Test B — East Scarp back to Town

1. Return from East Scarp through the same bridge route.
2. Confirm bridge return reaches Town near 118,72.
3. Confirm the player can walk away from the landing tile into the rest of Town.

### PASS

- return warp fires;
- Town loads correctly;
- landing tile is walkable;
- player is not trapped by SDS terrain or collision;
- no SMAPI error.

### FAIL classification

- `warp_missing`
- `warp_destination_wrong`
- `landing_blocked`
- `path_blocked_after_landing`
- `map_patch_visual_overlap`
- `runtime_exception_on_transition`
- `other`

---

# 4. SDS Avalia Forest access

The East Scarp route can be healthy while SDS's own Town connectivity is broken, so this must be tested separately.

## Test

- enter Avalia Forest using the normal SDS route from the current save state;
- return to the source location;
- repeat after visiting East Scarp in the same play session.

## PASS

- SDS warp exists in both directions;
- player lands on usable tiles;
- no SVE / East Scarp / Pelipper patch removes or masks the connection;
- no SMAPI exception occurs.

## FAIL evidence

Capture exact source/destination location names and the player's approximate tile or screenshot.

---

# 5. Pelipper Town integration sanity pass

Pelipper compatibility files integrate Pelipper with each expansion. They are not SDS patches, but they can still participate in a large-pack runtime failure.

For every installed Pelipper compatibility pack:

- confirm SMAPI loads the pack;
- confirm its required target expansion is actually installed;
- confirm no missing map/file error is reported;
- enter at least one route/location touched by that compatibility pack;
- check return travel, not only one-way travel.

Expected packs for the intended setup:

- `PelipperTown.SVE`
- `PelipperTown.EastScarp`
- `PelipperTown.RidgesideVillage`
- `PelipperTown.StarCrossed` only if StarCrossed is installed

A Pelipper integration failure must not automatically be labeled an SDS conflict until SDS involvement is reproduced.

---

# 6. Ridgeside Village runtime sanity pass

No hard SDS/RSV map collision has been established by the current research, so classify failures from evidence rather than assumption.

Minimum test:

- travel from vanilla/SVE world into RSV;
- return from RSV;
- enter Pelican Town before and after RSV travel;
- observe whether SDS Town remains usable;
- check SMAPI for schedule/path/map errors during the transitions.

If a conflict appears, record the exact location and event/time before building any patch.

---

# 7. NPC schedule and pathfinding checks

Static map compatibility does not prove schedule compatibility.

Test on at least:

- one normal weekday;
- one rainy day if practical;
- one day where SDS NPCs move through Pelican Town;
- one day where expansion NPCs enter or cross vanilla/SVE Town.

Watch for:

- NPC stuck against changed terrain;
- NPC repeatedly walking into an obstacle;
- NPC disappearing because a schedule target tile is invalid;
- schedule parse errors in SMAPI;
- pathfinding errors after Town map edits;
- two mods assigning incompatible route assumptions to the same vanilla area.

When a schedule issue occurs, record NPC name, day, time, source location, intended destination, and the first visible stuck point.

---

# 8. Festival validation

Large expansion packs often replace or patch festival maps and NPC placements independently of normal-day maps.

For each major vanilla festival reached during testing:

- festival starts successfully;
- festival map loads;
- player spawns correctly;
- SDS NPCs expected by the installed content appear where appropriate;
- expansion NPC additions do not cause visible stacking or inaccessible interaction tiles;
- festival can be completed/exited;
- returning to the normal world restores the correct Town/map state;
- SMAPI reports no festival-specific asset or placement error.

Prioritize any festival that occurs in or uses Pelican Town / Town-derived assets.

Do not build a festival compatibility patch unless the failure is reproducible on the same festival and mod set.

---

# 9. Runtime failure triage

When a failure is reproduced, classify it before editing files:

1. dependency/load problem;
2. Content Patcher condition problem;
3. asset missing / wrong target name;
4. map tile overlap;
5. lost/overwritten warp;
6. blocked landing tile;
7. schedule/pathfinding problem;
8. event/festival placement problem;
9. Pelipper integration problem unrelated to SDS;
10. unknown until log inspection.

Patch policy:

- prefer the smallest targeted compatibility patch;
- do not replace a whole map when a warp/area edit is sufficient;
- gate fixes behind the exact mod combination that requires them;
- avoid changing the already-working SVE/East Scarp route unless the runtime test proves it is broken;
- preserve SDS behavior when the conflict can be solved by rerouting the third-party entrance instead.

---

# 10. Completion rule for a runtime finding

A finding is not complete until all of the following are true:

- reproduced or explicitly marked non-reproducible;
- evidence is recorded;
- root cause is identified to a reasonable level;
- fix, if needed, is tested;
- regression route is re-tested;
- result is committed to GitHub;
- `CHECKPOINT.json`, `HANDOFF.md`, and compatibility research/handoff are updated when the finding changes project state.

## Immediate next input

The most useful next artifact is a **fresh full SMAPI log from the intended full modpack after loading a save and exercising the Town ↔ Shearwater Bridge ↔ East Scarp route**.
