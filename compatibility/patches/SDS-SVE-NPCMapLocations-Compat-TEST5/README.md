# SDS × SVE × NPC Map Locations Compatibility — TEST 5

## Root cause found

`Data/WorldMap` checks `WorldPositions` in order and uses the first matching entry.

Content Patcher adds new list entries at the bottom by default. In earlier tests the broad `Default` Town position therefore matched first, so custom Town bridge/east entries below it were never reached in some areas.

TEST 5 explicitly uses `MoveEntries` to force this order:

1. `VotriValley.SDS_BridgeCorridor`
2. `VotriValley.SDS_EastTown`
3. `Default`

## Runtime anchors that exposed the issue

- `Town 59,54`: user reports marker starts drifting here.
- `Town 74,53`: user reports marker is wrong on the small Town bridge.
- `Town 40,26`: previously validated as correct.
- Joja and SDS church anchors remain calibrated by the east-Town mapping.

## Bridge corridor

Tile area:

`X59..80, Y49..60`

Map pixel area:

`X180 Y80 Width38 Height8`

This is designed to connect smoothly to the validated west/default Town mapping at X58→59 and to SDS east Town at X80→81.

Predicted raw-map seam deltas:

- west seam X58→59: about `0.375px` X and `0.092px` Y;
- east seam X80→81: about `0.243px` X and `1.032px` Y.

This replaces the old ~100 runtime-pixel teleport behavior.

## East Town

Keeps:

`TileArea X80 Y0 Width93 Height116`

`MapPixelArea X216 Y54 Width48 Height65`

This preserves the Joja / SDS church calibration that tested well.

## Default Town

TEST 5 keeps the validated legacy Town scale by setting Default TileArea to:

`X0 Y0 Width80 Height116`

but does not rely on Default being sliced around the bridge. The custom bridge/east entries are moved before Default instead.

## Shearwater Bridge

The parent map-area hard override remains in TEST 5:

`Custom_ShearwaterBridge -> MapPixelArea X286 Y101 Width13 Height7`

## Install / test

Remove TEST 1–4 and install only TEST 5.

Important validation sequence:

1. Town `58,54`.
2. Walk slowly through `59,54` toward the bridge.
3. Continue through `74,53`, `80,53`, `81,53`.
4. Watch the minimap marker for continuous movement.
5. Verify `debug WorldMapPosition true` reports:
   - around X58: `Default`;
   - X59 through X80 while Y49–60: `VotriValley.SDS_BridgeCorridor`;
   - X81+: `VotriValley.SDS_EastTown`.
6. Recheck Joja, church, and `Custom_ShearwaterBridge`.
