# Session Handoff - 2026-09-12

## Current state

Seven Deadly Sins 3.13.4 Vietnamese text localization remains complete. Do not restart translation.

The active workstream is SDS + SVE + East Scarp runtime compatibility, NPC Map Locations world-map calibration, and SDS high-resolution portraits.

## East Scarp route

The preferred route is now confirmed conceptually as the native two-way chain:

`main world / railroad <-> Custom_ShearwaterBridge <-> EastScarp_Village`

Do not promote the old direct-route TEST 2, because its East Scarp return bypassed Shearwater Bridge and teleported directly to Town.

## NPC Map Locations / minimap

Installed tracker:

- NPC Map Locations 3.5.2
- UniqueID `Bouhm.NPCMapLocations`

The mod uses Stardew 1.6 `Data/WorldMap` / `WorldMapManager.GetPositionData()` for farmer placement.

### Runtime Town calibration

Measured anchors:

- Joja area: `Town 95,52`
- SDS church area: `Town 151,79`

NPC Map Locations TEST 1 split Town world-map mapping into west/central and east SDS regions. Runtime screenshot feedback indicates the Town marker now appears substantially correct.

### Shearwater Bridge finding

After TEST 1, entering `Custom_ShearwaterBridge` places the farmer marker visually on the SDS church.

Root cause is now identified precisely:

SVE already defines `Custom_ShearwaterBridge` in `Data/WorldMap` at:

`MapPixelArea X250 Y90 Width43 Height10`

Those coordinates fit SVE's own map artwork. SDS replaces the world-map artwork, and on the SDS artwork this same pixel region overlaps the church.

### Current minimap TEST 2

Source:

`compatibility/patches/SDS-SVE-NPCMapLocations-Compat-TEST2/`

TEST 2 keeps the working Town calibration and overrides only the Shearwater Bridge world-map area to:

`X286 Y101 Width13 Height7`

This moves the bridge marker to the far-east coast of the SDS world map instead of the church.

Latest source commits:

- manifest: `92f52cf2617ed25febcfe93edb556fa825d6283c`
- content: `870666117c3bdc6850c1cf212ffb7b90e0f3f75e`
- README: `9e051bbfad7b51bbdf53f0c13002e8e050187c8e`

### Exact next minimap action

1. Remove `[CP] SDS-SVE-NPCMapLocations-Compat-TEST1`.
2. Install `[CP] SDS-SVE-NPCMapLocations-Compat-TEST2`.
3. Restart the game completely.
4. Verify Town / Joja / church still align.
5. Enter `Custom_ShearwaterBridge` and confirm the marker moves to the far-east coast instead of the church.
6. If only slightly offset, fine-tune X/Y only. Do not redo Town calibration.

## SDS portraits / Portraiture

The user has already copied the SDS HD portrait PNGs to:

`Mods/Portraiture/Portraits/Seven Deadly Sins/`

Portraiture config and folder structure have been checked and are not the root cause of the oversized/cropped SDS portraits. Runtime log previously confirmed the active portrait set is `Seven Deadly Sins`.

The remaining portrait issue is in the runtime render/hook interaction between SDS's direct high-resolution portrait loads and Portraiture.

## Visual localization

Three Chinese statement screens are baked PNG assets, not JSON text:

- `SDS.statement1.png`
- `SDS.statement2.png`
- `SDS.statement3.png`

A Vietnamese visual hotfix test exists separately and still needs in-game confirmation before merging into the full release package.

## Persistence rule

Every confirmed runtime result or compatibility build must be committed before being called complete. Update CHECKPOINT.json and this handoff whenever the state changes.
