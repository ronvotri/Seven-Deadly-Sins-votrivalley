# SDS x SVE x NPC Map Locations Compatibility - TEST 3

## Status

TEST 1/2 established a working Town calibration. The remaining issue is `Custom_ShearwaterBridge`.

## Runtime evidence

With TEST 2 installed, `debug WorldMapPosition true` on `Custom_ShearwaterBridge` still reported:

`pixel area X1000 Y360 Width172 Height40`

Dividing by Stardew Valley's world-map zoom factor 4 yields:

`X250 Y90 Width43 Height10`

This exactly matches SVE's original Shearwater Bridge `MapPixelArea`, so the nested TEST 2 edit did not replace the SVE entry.

## TEST 3 strategy

Preserve the working Town calibration, but replace the entire SVE Shearwater Bridge map-area dictionary entry at:

`Data/WorldMap -> Valley -> MapAreas -> FlashShifter.StardewValleyExpanded_TownMap_ShearwaterBridge`

New bridge `MapPixelArea`:

`X286 Y101 Width13 Height7`

Expected runtime output after Stardew's x4 world-map zoom:

`X1144 Y404 Width52 Height28`

## Install

Remove both older packs first:

- `[CP] SDS-SVE-NPCMapLocations-Compat-TEST1`
- `[CP] SDS-SVE-NPCMapLocations-Compat-TEST2`

Then install:

- `[CP] SDS-SVE-NPCMapLocations-Compat-TEST3`

Restart the game completely.

## Validation

1. Confirm Town, Joja, and the SDS church remain aligned.
2. Enter `Custom_ShearwaterBridge`, preferably near tile `6,21`.
3. Run `debug WorldMapPosition true`.
4. Patch-application PASS: the pixel area is around `X1144 Y404 Width52 Height28` instead of `X1000 Y360 Width172 Height40`.
5. Check the minimap marker visually.

If the new area applies but is only a few pixels off, future work should tune only the bridge X/Y and preserve the Town calibration.
