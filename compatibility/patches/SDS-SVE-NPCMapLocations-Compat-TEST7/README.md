# SDS × SVE × NPC Map Locations Compatibility — TEST 7

## Runtime finding

The bridge is identified at runtime as:

- MapArea: `Custom_ShearwaterBridge`
- WorldPosition: `Custom_ShearwaterBridge`

Earlier tests incorrectly targeted SVE's Content Patcher patch-entry key rather than the runtime `Data/WorldMap` MapArea ID. As a result, the bridge stayed at SVE's original world-map pixel area.

## TEST 7 change

Target the runtime world-map object directly:

`Valley -> MapAreas -> Custom_ShearwaterBridge -> WorldPositions -> Custom_ShearwaterBridge`

Set bridge `MapPixelArea` to:

`X286 Y101 Width13 Height7`

Expected runtime pixel area at x4 scale:

`X1144 Y404 Width52 Height28`

## Town status

TEST 6 Town behavior is copied unchanged:

- calibrated Default Town mapping;
- BridgeCorridor before Default;
- EastTown before Default;
- Joja/church/Town corridor fixes preserved.

## Validation

Remove TEST 1 through TEST 6 and install only TEST 7. Restart the game fully.

On `Custom_ShearwaterBridge`, run:

`debug WorldMapPosition true`

`debug ppp`

PASS for patch application:

`pixel area is {X:1144 Y:404 Width:52 Height:28}`

If the old value remains:

`{X:1000 Y:360 Width:172 Height:40}`

then another later patch is overwriting the bridge world-map data and load-order tracing is required.
