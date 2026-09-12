# NPC Map Locations 3.5.2 — World Map Finding

Date: 2026-09-13

## Source inspected

User supplied `NPCMapLocations.rar` containing:

- NPC Map Locations 3.5.2
- UniqueID `Bouhm.NPCMapLocations`
- `NPCMapLocations.dll`
- `config.json`
- `assets/data.json`

The exact uploaded DLL contains references to:

- `WorldMapManager`
- `GetPositionData`
- `MapAreaPositionWithContext`
- `GetWorldMapPosition`

This matches Bouhm's current source implementation where NPC Map Locations resolves player/NPC positions through Stardew Valley 1.6's native world-map data:

`WorldMapManager.GetPositionData(location, tile)`

Therefore the farmer marker issue in the SDS+SVE setup is fundamentally a `Data/WorldMap` mapping problem, not a minimap X/Y config problem.

## Important correction to previous plan

The old integration target:

`Mods/Bouhm.NPCMapLocations/Locations`

is still loaded by NPC Map Locations 3.5.2, but current code only consumes location exclusions from that asset. It does **not** use legacy `MapVectors` there to calculate the farmer marker position.

So a compatibility patch which only edits `Mods/Bouhm.NPCMapLocations/Locations` / `MapVectors` would not fix the current farmer marker offset.

## Correct patch target

For NPC Map Locations 3.5.2, the correct compatibility target is:

`Data/WorldMap`

because NPC Map Locations delegates coordinate resolution to the game's `WorldMapManager`.

## Why SDS can break the marker

SDS 3.13.4 heavily changes the geometry/layout of `Town` while the active world-map position data can still correspond to vanilla/SVE Town topology. The in-world tile position remains valid, but the world-map pixel produced for that tile can point to the wrong visual place on the minimap.

## Best runtime diagnostic

Stardew Valley 1.6.15 includes a built-in debug command specifically for this system:

`debug WorldMapPosition true`

Run it while standing at a visibly incorrect marker position. It logs:

- current location;
- current tile;
- world-map area/position match;
- computed map pixel;
- detailed matching log.

Also run:

`debug ppp`

at the same position.

With this output, derive the smallest `Data/WorldMap` compatibility patch for the SDS-modified Town instead of guessing offsets.

## Current status

- issue reproduced visually: yes
- NPC Map Locations exact version confirmed: 3.5.2
- mechanism confirmed: `WorldMapManager.GetPositionData`
- legacy `MapVectors`-only fix rejected
- correct target: `Data/WorldMap`
- patch values: pending runtime `debug WorldMapPosition true` output
