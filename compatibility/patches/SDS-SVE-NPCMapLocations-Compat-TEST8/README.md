# SDS × SVE × NPC Map Locations Compatibility — TEST 8

TEST 7 still left `Custom_ShearwaterBridge` at the original SVE runtime world-map area:

`X1000 Y360 Width172 Height40`

TEST 8 switches the bridge edit to Content Patcher's documented list-safe pattern: target the parent `WorldPositions` list and edit the existing `Custom_ShearwaterBridge` model through `Fields` keyed by its `Id`.

Town calibration from TEST 6 is preserved unchanged.

Expected bridge runtime after TEST 8:

`X1144 Y404 Width52 Height28`

## Install

Remove TEST 1 through TEST 7 and install only:

`[CP] SDS-SVE-NPCMapLocations-Compat-TEST8`

Restart Stardew Valley completely.

## Validate

In Town near X62,Y54, `debug WorldMapPosition true` should still match `VotriValley.SDS_BridgeCorridor`.

On `Custom_ShearwaterBridge`, run:

`debug WorldMapPosition true`

`debug ppp`

PASS if the bridge pixel area is approximately `X1144 Y404 Width52 Height28`.

If Town custom entries appear but the bridge remains `X1000 Y360 Width172 Height40`, the pack is loading and a later `Data/WorldMap` patch is overwriting only the bridge entry; the next step is load-order tracing rather than coordinate tuning.
