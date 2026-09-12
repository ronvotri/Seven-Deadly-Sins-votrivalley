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

**CONFIRMED RUNTIME ACCESS CONFLICT — compatibility patch required.**

## TEST 1 patch strategy

Minimal corridor patch only:

- target: `Maps/Town`
- clear `Buildings` layer only
- rectangle: X111 Y73 W3 H2
- preserve Back, warp properties, Shearwater Bridge, East Scarp Village, and SDS Avalia Forest
- gate the content pack behind SDS + SVE + East Scarp dependencies

TEST 1 must be validated in game before expanding the corridor or making a release patch.
