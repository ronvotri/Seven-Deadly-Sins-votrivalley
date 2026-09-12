# Runtime Finding — East Town route blocked

Date: 2026-09-12

## Reproduced setup

User runtime test with SDS 3.13.4 + SVE + East Scarp in the intended large modpack.

## Exact runtime coordinate

SMAPI `debug ppp` result at the west side of the blockage:

`Town X110 Y73`

## Source confirmation

SDS with SVE applies `Maps/Compatible/SDS.Town.Main*.tmx` to `Maps/Town` at `X110 Y0 W63 H116` with `Priority: Late`.

In the normal `SDS.Town.Main.tmx` variant, the route immediately east of the user's position contains `Buildings` tiles at:

- X111 Y73
- X112 Y73
- X113 Y73
- X111 Y74
- X112 Y74
- X113 Y74

The SVE outgoing Shearwater warp strip remains farther east at X119 Y72–76, so the warp itself can exist while access to it is blocked by SDS terrain/buildings.

## Revised compatibility classification

The previous static finding "warp strip itself is walkable" was too narrow. Runtime testing confirms the practical route is blocked before the warp strip.

Classification for the tested setup is now:

**CONFIRMED RUNTIME ACCESS / TOPOLOGY CONFLICT — compatibility patch required.**

## TEST 1 result — rejected

TEST 1 cleared only the Buildings layer at:

`Town X111 Y73 W3 H2`

Runtime retest showed this was not sufficient. The user still could not reach East Scarp and the combined Town presentation showed broader map/topology overlap around the old route.

Therefore the TEST 1 strategy is rejected. Do not expand the same corridor blindly.

## Chosen strategy — direct reroute

The user chose to stop using the old practical route:

`Town -> Custom_ShearwaterBridge -> EastScarp_Village`

for this compatibility patch.

Instead, use a direct two-way route:

`Town <-> EastScarp_Village`

This avoids editing the overlapped Town terrain and avoids depending on `Custom_ShearwaterBridge` for this mod combination.

## TEST 2

Source:

`compatibility/patches/SDS-SVE-EastScarp-DirectRoute-TEST2/`

Town direct gate:

- `110,72 -> EastScarp_Village 1,71`
- `110,73 -> EastScarp_Village 1,72`
- `110,74 -> EastScarp_Village 1,73`

Return gate:

- `EastScarp_Village X0,Y70-74 -> Town X109,Y72-74`

The return landing uses X109 intentionally so returning to Town does not immediately retrigger the direct warp at X110.

TEST 2 edits warps only and does not modify Town Back/Buildings/Front layers.

## Current status

**TEST 2 BUILT — two-way runtime validation pending.**

Next validation:

1. remove TEST 1;
2. test Town -> EastScarp_Village directly at Town X110,Y72-74;
3. test EastScarp_Village west edge -> Town;
4. confirm both landing areas are walkable;
5. if either trigger fails, capture `debug ppp` at the exact failed tile and a fresh SMAPI log if Content Patcher reports errors.
