# Session Handoff - 2026-09-14

## Current state

Seven Deadly Sins 3.13.4 Vietnamese text localization remains complete. Do not restart translation.

Active workstreams:

- SDS + SVE + East Scarp runtime compatibility;
- NPC Map Locations world-map calibration;
- SDS high-resolution portrait rendering;
- Vietnamese replacement for three baked Chinese statement PNGs.

## East Scarp route

Preferred route remains:

`main world / railroad <-> Custom_ShearwaterBridge <-> EastScarp_Village`

Do not restore the rejected direct-route TEST 2 because it made the return path jump directly from East Scarp to Town.

## NPC Map Locations / minimap

Installed tracker:

- NPC Map Locations 3.5.2
- UniqueID `Bouhm.NPCMapLocations`

The mod uses Stardew 1.6 `Data/WorldMap` / `WorldMapManager.GetPositionData()`.

### Confirmed anchors and findings

Runtime anchors:

- Town `40,26`: visually correct under the calibrated legacy/default mapping;
- Town `39,58`: resolves `Default`;
- Town `58,53`: resolves `Default`;
- Town `62,54`: resolves `VotriValley.SDS_BridgeCorridor` under TEST 5;
- Town `69,53`: resolves `VotriValley.SDS_BridgeCorridor` under TEST 5;
- Town `74,54`: resolves `VotriValley.SDS_BridgeCorridor` under TEST 5;
- Joja area around Town `95,52`: east calibration good;
- SDS church around Town `151,79`: east calibration good.

### Root cause 1: WorldPosition ordering

`WorldPositions` is order-sensitive. Stardew uses the first matching position. Content Patcher appends new list entries by default, so custom zones can sit below broad `Default` and never be evaluated.

TEST 5 fixed this with `MoveEntries`, enforcing:

1. `VotriValley.SDS_BridgeCorridor`
2. `VotriValley.SDS_EastTown`
3. `Default`

Runtime confirmed the ordering fix works because Town `62,54`, `69,53`, and `74,54` all matched `SDS_BridgeCorridor`.

### Root cause 2: Default projection reverted too wide in TEST 5

TEST 5 accidentally allowed Town `Default` to use SVE's wide projection:

`runtime pixel area X588 Y184 Width388 Height320`

This made the marker too far right before entering the corridor, so it still appeared to jump when transitioning from Default into BridgeCorridor.

The correct calibrated Town Default projection used in earlier successful tests is:

- raw `MapPixelArea X147 Y46 Width45 Height80`
- runtime `X588 Y184 Width180 Height320`

## Current minimap TEST 6

Source:

`compatibility/patches/SDS-SVE-NPCMapLocations-Compat-TEST6/`

Source commits:

- manifest: `1c68538e67d319203dfaf796643eaf3568bc155d`
- content: `48d8752d29dd14e239a70b7594cb90cdb2cb7445`
- README: `9193c0727a7efc7c13fac487343d4a7f9775418f`

### TEST 6 behavior

1. Explicitly restores Town `Default`:

`TileArea X0 Y0 Width80 Height116`

`MapPixelArea X147 Y46 Width45 Height80`

2. Keeps ordered custom zones before Default.

Bridge corridor:

`TileArea X59 Y49 Width22 Height12`

`MapPixelArea X180 Y80 Width38 Height8`

East Town:

`TileArea X80 Y0 Width93 Height116`

`MapPixelArea X216 Y54 Width48 Height65`

3. Keeps hard override for `Custom_ShearwaterBridge`:

`MapPixelArea X286 Y101 Width13 Height7`

### Expected TEST 6 continuity

At Town `58,53` under Default:

- runtime position about `(718.50, 330.21)`

At Town `59,53` under BridgeCorridor:

- runtime position about `(720.00, 330.67)`

Expected seam delta is only about +1.5 px horizontally and +0.46 px vertically.

## Exact next minimap action

1. Remove minimap TEST 1 through TEST 5.
2. Install only TEST 6.
3. Restart game fully.
4. At Town `58,53`, run `debug WorldMapPosition true`.
5. PASS prerequisite: `Default` pixel area must be `X588 Y184 Width180 Height320`, not Width388.
6. Walk slowly `X58 -> X59 -> X62 -> X69 -> X74 -> X80 -> X81` around Y53-54.
7. Confirm marker movement is continuous.
8. Recheck Joja, church, and `Custom_ShearwaterBridge`.

## Portraits

The user's Portraiture config, folder structure, active set, and portrait dimensions have been checked. Runtime previously confirmed active set `Seven Deadly Sins`.

Remaining portrait issue is runtime rendering / hook interaction with SDS direct HD portrait loads.

## Visual localization

Three Chinese statement screens are baked PNG assets:

- `SDS.statement1.png`
- `SDS.statement2.png`
- `SDS.statement3.png`

A Vietnamese visual hotfix test exists and still needs final in-game confirmation before merging into the full release package.

## Persistence rule

Every confirmed runtime result or compatibility build must be committed before being called complete. Update CHECKPOINT.json and this handoff whenever state changes.
