# Runtime Finding — 2026-09-11 — East route blocked in full modpack

## Status

**CONFIRMED RUNTIME FAILURE IN THE USER'S FULL MODPACK. ROOT CAUSE NOT YET ATTRIBUTED TO A SINGLE MOD.**

The user tested the intended large modpack in Stardew Valley 1.6.15 with SMAPI 4.5.2 and reported that the east-side route toward `Custom_ShearwaterBridge -> EastScarp_Village` is not physically reachable. The supplied in-game screenshot shows the Town east-side approach obstructed by terrain/fence/vegetation.

This supersedes any interpretation of the earlier static audit as proof that the full modpack route is usable at runtime.

## Important distinction

The earlier source audit remains valid only for the specific SDS/East Scarp/SVE geometry that was inspected:

- SDS 3.13.4 source variants did not place a Buildings-layer blocker directly on Town X119,Y72-76.
- East Scarp 3.0.9 with SVE routes through `Custom_ShearwaterBridge`.

The runtime screenshot proves that the **composed final Town map in the user's full modpack** is nevertheless blocked before the route can be used.

Because the live setup contains many additional mods, the blocker must not be attributed to SDS alone until current patch order and final map composition are inspected.

## Required next evidence

1. Fresh complete `SMAPI-latest.txt` from the exact run that reproduced the blocked route.
2. Preferably Content Patcher exports after loading the affected save:
   - `patch export Maps/Town`
   - `patch export Maps/Custom_ShearwaterBridge`
3. Exact installed versions of SVE, East Scarp, SDS and any Town-editing content packs from that run.

## Patch policy

Do not remove large SDS Town areas pre-emptively.

After the blocker is identified, build the smallest gated compatibility patch that restores a walkable path and preserves:

- SVE Town layout;
- East Scarp Shearwater connection;
- SDS Town content and Avalia Forest route;
- unrelated Town edits from the rest of the modpack where possible.

## Evidence origin

User-supplied runtime screenshot and direct gameplay report in the 2026-09-11 compatibility validation session.
