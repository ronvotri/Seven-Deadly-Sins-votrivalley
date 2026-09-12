# SDS × SVE × East Scarp Direct Route — TEST 2

This test patch abandons the broken practical route through `Custom_ShearwaterBridge` for the tested large modpack and adds a direct two-way route:

`Town <-> EastScarp_Village`

## Why TEST 2 exists

Runtime testing confirmed that the east-Town route is not merely blocked by one Buildings strip. The combined final Town topology is visually and functionally inconsistent around the old Shearwater access. TEST 1 only cleared a small Buildings corridor and did not solve the real route problem.

Therefore TEST 2 does not edit Town terrain at all. It adds direct warps only.

## Town -> East Scarp

- Town `110,72` -> `EastScarp_Village 1,71`
- Town `110,73` -> `EastScarp_Village 1,72`
- Town `110,74` -> `EastScarp_Village 1,73`

The user already confirmed they can reach Town `110,73` via `debug ppp`.

## East Scarp -> Town

- EastScarp_Village west edge `0,70-74` -> Town `109,72-74`

The return destination intentionally uses Town X109 rather than X110 so the player is not immediately sent back into East Scarp after returning.

## Test requirements

Remove the old TEST 1 content pack before testing this build.

Test both directions:

1. Town -> EastScarp_Village without entering Custom_ShearwaterBridge;
2. EastScarp_Village west edge -> Town;
3. confirm arrival tiles are walkable;
4. capture `debug ppp` at any failed trigger/landing point;
5. capture a fresh SMAPI log if Content Patcher reports errors.

## Status

`TEST 2 — runtime validation pending`
