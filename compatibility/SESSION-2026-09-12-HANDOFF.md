# Session Handoff - 2026-09-12

## Current state

Seven Deadly Sins 3.13.4 Vietnamese text localization remains complete. Do not restart translation.

The active workstream is SDS + SVE + East Scarp runtime compatibility, NPC Map Locations world-map calibration, and SDS high-resolution portraits.

## East Scarp route

Preferred route remains the native two-way chain:

`main world / railroad <-> Custom_ShearwaterBridge <-> EastScarp_Village`

Do not restore the old direct-route TEST 2 because it created an asymmetric East Scarp -> Town teleport.

## NPC Map Locations / minimap

Installed tracker:

- NPC Map Locations 3.5.2
- UniqueID `Bouhm.NPCMapLocations`

The mod uses Stardew 1.6 `Data/WorldMap` / `WorldMapManager.GetPositionData()` for farmer placement.

### Town calibration

Measured runtime anchors:

- Joja area: `Town 95,52`
- SDS church area: `Town 151,79`

The split Town mapping introduced in TEST 1/2 appears substantially correct in runtime. Preserve it.

### Shearwater Bridge runtime finding

After TEST 2, the user tested `Custom_ShearwaterBridge` at tile `6,21`.

`debug WorldMapPosition true` reported:

`pixel area X1000 Y360 Width172 Height40`

with player ratio approximately `X0.1 Y0.525`.

Dividing the pixel area by Stardew's x4 world-map zoom gives exactly:

`X250 Y90 Width43 Height10`

which is SVE's original Shearwater Bridge `MapPixelArea`.

Therefore TEST 2's nested edit did not replace the SVE world-map entry. The bridge marker is still using SVE coordinates on SDS artwork, which visually lands around the SDS church.

## Current minimap TEST 3

Source:

`compatibility/patches/SDS-SVE-NPCMapLocations-Compat-TEST3/`

TEST 3 preserves the working Town calibration and replaces the entire SVE Shearwater Bridge map-area dictionary entry at:

`Data/WorldMap -> Valley -> MapAreas -> FlashShifter.StardewValleyExpanded_TownMap_ShearwaterBridge`

New raw bridge placement:

`X286 Y101 Width13 Height7`

Expected `debug WorldMapPosition true` pixel area after x4 zoom:

`X1144 Y404 Width52 Height28`

TEST 3 source commits:

- manifest: `e481098b3100850194c4a7eb50cd9c8bf85a17b8`
- content: `02f962496962a9527f70d4b742b2e64df3566e55`
- README: `dba108fbd282162ef1baf5bc0cd22da59922494e`

### Exact next minimap action

1. Remove `[CP] SDS-SVE-NPCMapLocations-Compat-TEST1` and `[CP] SDS-SVE-NPCMapLocations-Compat-TEST2`.
2. Install `[CP] SDS-SVE-NPCMapLocations-Compat-TEST3`.
3. Restart the game completely.
4. Verify Town / Joja / church remain correct.
5. Enter `Custom_ShearwaterBridge`, preferably near tile `6,21`.
6. Run `debug WorldMapPosition true`.
7. PASS for patch application: pixel area changes from `X1000 Y360 Width172 Height40` to approximately `X1144 Y404 Width52 Height28`.
8. If visually only a few pixels off after that, tune only bridge X/Y. Do not redo Town calibration.

## SDS portraits / Portraiture

The user has already copied the SDS HD portrait PNGs to:

`Mods/Portraiture/Portraits/Seven Deadly Sins/`

Portraiture config, folder structure, and active set have been verified. Runtime previously confirmed active portrait set `Seven Deadly Sins`.

The remaining portrait issue is in runtime rendering / hook interaction with SDS's direct high-resolution portrait loads.

## Visual localization

Three Chinese statement screens are baked PNG assets, not JSON text:

- `SDS.statement1.png`
- `SDS.statement2.png`
- `SDS.statement3.png`

A Vietnamese visual hotfix test exists separately and still needs in-game confirmation before merging into the full release package.

## Persistence rule

Every confirmed runtime result or compatibility build must be committed before being called complete. Update CHECKPOINT.json and this handoff whenever the state changes.
