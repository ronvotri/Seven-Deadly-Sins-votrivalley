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

### Confirmed Town anchors

Runtime anchors gathered from the user's modpack:

- Town `40,26`: visually correct under legacy/default mapping;
- Town `59,54`: marker starts drifting;
- Town `74,53`: small Town bridge marker visibly wrong;
- Town `79,53` and `80,53`: earlier tests exposed a severe one-tile discontinuity;
- Joja area around Town `95,52`: east calibration good;
- SDS church around Town `151,79`: east calibration good.

### Root cause found on 2026-09-14

`WorldPositions` is an ordered list. Stardew checks positions in order and uses the first matching entry.

Content Patcher appends new list entries at the bottom by default. Earlier custom entries such as `VotriValley.SDS_EastTown` or lower/bridge zones could therefore sit below broad Town `Default`; when `Default` matched first, the custom entry was never evaluated.

This explains why debug output at Town `59,54` and `74,53` continued to report `Default` even though custom zones existed in the patch.

The correct Content Patcher mechanism is `MoveEntries`.

## Current minimap TEST 5

Source:

`compatibility/patches/SDS-SVE-NPCMapLocations-Compat-TEST5/`

Source commits:

- manifest: `b2963e825a25b6e50697c4ddaf79d738c71947ef`
- content: `388538f3c6a0cf2cccb22421336a0de9dd9de647`
- README: `6fd893b3db66893cf4c590c11857981041cdee07`

### Town order enforced by TEST 5

1. `VotriValley.SDS_BridgeCorridor`
2. `VotriValley.SDS_EastTown`
3. `Default`

`MoveEntries` puts both custom entries before `Default`.

### Bridge corridor

TileArea:

`X59 Y49 Width22 Height12`

MapPixelArea:

`X180 Y80 Width38 Height8`

Expected continuity:

- Default `Town 58,54` -> raw map about `(179.625, 83.241)`;
- Corridor `Town 59,54` -> `(180.000, 83.333)`;
- Corridor `Town 80,53` -> about `(216.273, 82.667)`;
- EastTown `Town 81,53` -> about `(216.516, 83.698)`.

The old ~100 runtime-pixel teleport should disappear.

### East Town

Keep validated calibration:

`TileArea X80 Y0 Width93 Height116`

`MapPixelArea X216 Y54 Width48 Height65`

### Default Town

Default TileArea remains constrained to:

`X0 Y0 Width80 Height116`

This preserves the west/central Town scale that tested correctly at `Town 40,26`.

### Custom_ShearwaterBridge

TEST 5 retains the parent map-area hard override:

`MapPixelArea X286 Y101 Width13 Height7`

## Exact next minimap action

1. Remove minimap TEST 1–4.
2. Install only TEST 5.
3. Restart game fully.
4. At Town around Y53–54, walk slowly:
   `X58 -> X59 -> ... -> X74 -> ... -> X80 -> X81`.
5. Watch minimap marker for continuous motion.
6. Run `debug WorldMapPosition true` at representative points.
7. PASS expectation:
   - around X58: `Default`;
   - X59–80 while Y49–60: `VotriValley.SDS_BridgeCorridor`;
   - X81+: `VotriValley.SDS_EastTown`.
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
