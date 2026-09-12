# Session Handoff — 2026-09-12

## Current state

Seven Deadly Sins 3.13.4 Vietnamese text localization remains complete. Do not restart translation.

The active workstream is SDS × SVE × East Scarp runtime compatibility plus two separate presentation issues: NPC Map Locations coordinate mapping and SDS high-resolution portraits.

## East route runtime history

Initial runtime blockage was reproduced at:

`Town X110 Y73`

TEST 1 cleared a tiny Buildings corridor at X111 Y73 W3 H2 and failed. Do not retry or blindly enlarge it.

TEST 2 added direct Town <-> EastScarp_Village warps. Runtime testing showed the user already has an acceptable forward route through the normal railroad / Shearwater Bridge chain, while TEST 2 makes the reverse direction jump directly from East Scarp to Town.

### Current decision

**TEST 2 is rejected and must not be promoted.**

Preferred route:

`main world / railroad -> Custom_ShearwaterBridge -> EastScarp_Village`

and the same path in reverse.

Immediate route action:

1. remove `[CP] SDS-SVE-EastScarp-DirectRoute-TEST2`;
2. restart the game;
3. enter East Scarp through the working railroad / Shearwater Bridge path;
4. test the native EastScarp_Village -> Custom_ShearwaterBridge -> main-world return;
5. only build another warp patch if that native return still fails without TEST 2.

Canonical updated finding:

`compatibility/RUNTIME-FINDING-2026-09-12-BRIDGE-MINIMAP-PORTRAITURE.md`

## Minimap issue

Installed minimap/world-map tracker from the tested setup:

- NPC Map Locations 3.5.2
- UniqueID `Bouhm.NPCMapLocations`

Farmer position is visually wrong on the minimap/world map.

This is a separate coordinate-mapping compatibility issue. NPC Map Locations uses `Data/WorldMap` when available and map/warp-derived relationships otherwise. SDS changes Town topology significantly, so vanilla/SVE map-coordinate assumptions may no longer match the final Town layout.

Do not guess `MapVectors`.

Next minimap work:

- derive the correct final Town mapping vectors for the SDS+SVE Town layout;
- then build a small Content Patcher compatibility pack targeting `Mods/Bouhm.NPCMapLocations/Locations` or the appropriate `Data/WorldMap` entry;
- validate player marker at multiple Town coordinates, not just one tile.

## SDS portraits / Portraiture

SDS ships high-resolution portrait PNGs and its own readme lists Portraiture as the PC HD portrait prerequisite.

The user has already copied SDS portrait PNGs to:

`Mods/Portraiture/Portraits/Seven Deadly Sins/`

To avoid pressing P repeatedly, set Portraiture's active set in:

`Mods/Portraiture/config.json`

so the `active` value exactly matches:

`Seven Deadly Sins`

Portraiture saves the chosen active set, so once configured the SDS portraits should be used automatically after reload.

Portraiture also has an optional large-above-dialogue display mode. If the user wants normal dialogue-box sizing rather than an intentionally enlarged above-box portrait, keep that mode disabled.

## Other open SDS item

Three Chinese statement screens are baked PNG assets, not JSON text:

- `SDS.statement1.png`
- `SDS.statement2.png`
- `SDS.statement3.png`

A Vietnamese visual hotfix test exists separately.

## Exact next action

1. Remove TEST 2 and confirm the native bridge return path.
2. Configure Portraiture active set to `Seven Deadly Sins` and restart, then verify Raymond/Maria/Edward display without manual P switching.
3. For minimap calibration, gather at least two or three known Town tile positions (`debug ppp`) together with where the farmer marker appears on the world map/minimap. Use those points to derive a proper NPC Map Locations mapping instead of guessing.

## Persistence rule

Every confirmed runtime result or compatibility build must be committed before being called complete. Update CHECKPOINT.json and the handoff when the state changes.
