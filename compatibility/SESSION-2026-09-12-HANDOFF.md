# Session Handoff - 2026-09-14

## Current state

Seven Deadly Sins 3.13.4 Vietnamese text localization remains complete. Do not restart translation.

Active workstreams:

- SDS + SVE + East Scarp runtime compatibility;
- SDS high-resolution portrait rendering;
- Vietnamese replacement for three baked Chinese statement PNGs.

NPC Map Locations minimap calibration is now **deferred by user decision**. Do not resume it automatically.

## East Scarp route

Preferred route remains:

`main world / railroad <-> Custom_ShearwaterBridge <-> EastScarp_Village`

Do not restore the rejected direct-route TEST 2 because it made the return path jump directly from East Scarp to Town.

## NPC Map Locations / minimap — DEFERRED

Installed tracker:

- NPC Map Locations 3.5.2
- UniqueID `Bouhm.NPCMapLocations`

The mod uses Stardew 1.6 `Data/WorldMap` / `WorldMapManager.GetPositionData()`.

A long calibration series (TEST 1 through TEST 8) improved some Town positions, but the combined SDS + SVE world-map geometry still produced inconsistent marker placement, especially around Town bridge transitions and `Custom_ShearwaterBridge`.

### Final user decision

The user explicitly chose to stop minimap compatibility work for now and accept the original NPC Map Locations behavior as a temporary known limitation.

### Practical state

- Remove all custom minimap compatibility packs TEST 1 through TEST 8.
- Keep the original NPC Map Locations mod unchanged.
- Restart the game completely after removal.
- The minimap may show inaccurate farmer position in some SDS/SVE areas; this is accepted for now.
- Do not build TEST 9 or resume coordinate tuning unless the user explicitly asks to revisit this feature.

### Findings worth preserving if revisited later

- Town `WorldPositions` are order-sensitive; custom entries may need `MoveEntries` before broad `Default`.
- TEST 5 confirmed custom `SDS_BridgeCorridor` matching at Town `62,54`, `69,53`, and `74,54`.
- SVE `Default` projection can report runtime `X588 Y184 Width388 Height320`, which conflicts with the narrower SDS-calibrated projection.
- `Custom_ShearwaterBridge` continued to report SVE's original runtime pixel area `X1000 Y360 Width172 Height40` through later tests.
- The last attempted strategy was TEST 8 using parent-list `Fields` targeting for the bridge, but the user stopped testing before validation.

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
