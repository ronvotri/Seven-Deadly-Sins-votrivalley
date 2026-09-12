# Session Handoff — 2026-09-12

## Current state

Seven Deadly Sins 3.13.4 Vietnamese text localization remains complete. Do not restart translation.

The active workstream is now **SDS × SVE × East Scarp runtime compatibility**.

## Runtime finding that overrides the old static-only conclusion

Static inspection previously found that the SVE Shearwater warp strip itself survives SDS tile edits. Runtime testing proved that this was not enough: the practical east-Town route is blocked/overlapped before the player can reach that warp strip.

Exact user runtime coordinate at the blockage:

`Town X110 Y73`

Canonical finding:

`compatibility/RUNTIME-FINDING-2026-09-12-EAST-TOWN-BLOCK.md`

Classification for the tested large modpack:

**CONFIRMED RUNTIME ACCESS / TOPOLOGY CONFLICT — patch required.**

## TEST 1

Strategy:

- clear Buildings at Town X111 Y73 W3 H2

Result:

**FAILED / REJECTED.**

The player still could not use the practical route and the combined Town presentation showed broader topology overlap. Do not keep enlarging this corridor blindly.

## User decision

The user explicitly chose a direct reroute:

`Town -> EastScarp_Village`

instead of preserving:

`Town -> Custom_ShearwaterBridge -> EastScarp_Village`

for this compatibility pack.

## TEST 2 — current build

Source:

`compatibility/patches/SDS-SVE-EastScarp-DirectRoute-TEST2/`

Builder:

`compatibility/patches/build_direct_route_test2.py`

Town gate:

- X110,Y72 -> EastScarp_Village 1,71
- X110,Y73 -> EastScarp_Village 1,72
- X110,Y74 -> EastScarp_Village 1,73

Return gate:

- EastScarp_Village X0,Y70-74 -> Town X109,Y72-74

Return uses Town X109 intentionally to avoid immediate bounce-back into the direct Town gate at X110.

TEST 2 modifies warps only. It does not edit Town Back/Buildings/Front layers.

Current TEST 2 status:

**BUILT — two-way runtime validation pending.**

## Exact next action

1. Ensure TEST 1 is removed.
2. Install TEST 2 only.
3. Test Town -> EastScarp_Village at Town X110,Y72-74.
4. Confirm it skips Custom_ShearwaterBridge entirely.
5. Test EastScarp_Village west edge -> Town.
6. Confirm landing at Town X109 is walkable and does not bounce back.
7. If either direction fails, capture `debug ppp` at the exact failed trigger/landing tile.
8. Capture a fresh full SMAPI log if Content Patcher reports an error.

## Promotion rule

Do not promote TEST 2 to a stable/release compatibility pack until both directions pass runtime validation.

After both directions pass:

- move to a stable UniqueID;
- package a release candidate;
- optionally add visual entrance treatment without changing the working warp topology;
- regression-test Avalia Forest access and the rest of the large expansion stack.

## Other open SDS items

### Visual localization

Three Chinese statement screens are baked PNG assets, not JSON text:

- `SDS.statement1.png`
- `SDS.statement2.png`
- `SDS.statement3.png`

A Vietnamese visual hotfix test has been built separately. Do not confuse this with the East Scarp compatibility pack.

### Portraits

SDS uses high-resolution portrait assets. The user has moved them to Portraiture as instructed. Treat portrait display as a separate setup issue, not part of the direct-route patch.

## Persistence rule

Every confirmed runtime result and compatibility build must be committed before being called complete. Update `CHECKPOINT.json`, root `HANDOFF.md`, and this handoff or a newer session handoff when the runtime state changes.
