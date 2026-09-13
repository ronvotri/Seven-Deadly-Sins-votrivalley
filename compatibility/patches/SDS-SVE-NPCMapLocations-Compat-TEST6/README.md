# SDS × SVE × NPC Map Locations Compatibility — TEST 6

## What TEST 5 confirmed

The ordering fix worked:

- Town `62,54` -> `VotriValley.SDS_BridgeCorridor`
- Town `69,53` -> `VotriValley.SDS_BridgeCorridor`
- Town `74,54` -> `VotriValley.SDS_BridgeCorridor`

But `Default` reverted to SVE's wide projection:

`runtime pixel area X588 Y184 Width388 Height320`

That caused the marker to be too far right before entering the corridor.

## TEST 6 fix

Restore the calibrated Town Default MapPixelArea:

- raw: `X147 Y46 Width45 Height80`
- runtime: `X588 Y184 Width180 Height320`

Keep TEST 5's correct WorldPosition order:

1. `VotriValley.SDS_BridgeCorridor`
2. `VotriValley.SDS_EastTown`
3. `Default`

Keep the validated East Town and Shearwater Bridge fixes.

## Expected continuity

Town `58,53` under Default:

- runtime X about `718.50`
- runtime Y about `330.21`

Town `59,53` under BridgeCorridor:

- runtime X `720.00`
- runtime Y about `330.67`

So crossing X58 -> X59 should move only about 1.5 pixels horizontally and 0.46 pixels vertically.

## Install

Remove minimap TEST 1 through TEST 5.

Install only:

`[CP] SDS-SVE-NPCMapLocations-Compat-TEST6`

Restart Stardew Valley completely.

## Test

1. Check Town `39,58`.
2. Check Town `58,53`.
3. Walk `X58 -> X59 -> X62 -> X69 -> X74 -> X80 -> X81`.
4. Recheck Joja, church, and `Custom_ShearwaterBridge`.

Useful commands:

`debug WorldMapPosition true`

`debug ppp`

Expected at Town `58,53`:

`Default` pixel area must be `X588 Y184 Width180 Height320`.

If it still reports `Width388`, TEST 6 is not being applied.
