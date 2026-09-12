# HANDOFF - Seven Deadly Sins 3.13.4

> **Vietnamese text localization is complete. Active work is runtime compatibility. Do not restart translation unless a new source version or an in-game localization bug appears.**

## Localization status

- CP: **24,827 / 24,827**, clean audit, canonical commit `2ca310f`
- DLL: **2,419 / 2,419**, clean audit, canonical commit `c2e0461693e423785a6dc4ea44eb5fc430b84949`
- Release archive: `dist/Seven-Deadly-Sins-3.13.4-Vietnamese-Localization.zip`

## Current compatibility source of truth

Read first:

`compatibility/SESSION-2026-09-12-HANDOFF.md`

Then:

`compatibility/RUNTIME-FINDING-2026-09-12-EAST-TOWN-BLOCK.md`

Historical/static map research:

`compatibility/SDS-EastScarp-SVE-RESEARCH.md`

Important: the old static conclusion that the Shearwater warp strip itself remained walkable is **not** the current runtime conclusion. Runtime testing superseded it for the tested modpack.

---

# CURRENT RUNTIME CLASSIFICATION

Target stack includes SDS 3.13.4 + SVE + East Scarp 3.0.9 in the user's large modpack.

User runtime coordinate at the east-Town blockage:

`Town X110 Y73`

The original practical route:

`Town -> Custom_ShearwaterBridge -> EastScarp_Village`

is confirmed unusable in the tested combined runtime state because the final Town topology is blocked/overlapped before the player can reach the old SVE warp strip.

Classification:

**CONFIRMED RUNTIME ACCESS / TOPOLOGY CONFLICT — compatibility patch required.**

## TEST 1

Cleared Buildings at Town X111 Y73 W3 H2.

Result:

**REJECTED.** The route remained unusable and broader map overlap was visible. Do not continue enlarging that corridor blindly.

## TEST 2 — Direct Route

The user chose to bypass Shearwater completely for this compatibility pack.

New route:

`Town <-> EastScarp_Village`

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

Return lands on X109 intentionally to prevent instant bounce-back into the Town gate at X110.

TEST 2 edits warps only. No Town terrain layers are modified.

Status:

**BUILT — two-way runtime validation pending.**

---

# EXACT NEXT ACTION

1. Remove TEST 1.
2. Install TEST 2 only.
3. Test Town -> EastScarp_Village through Town X110,Y72-74.
4. Confirm `Custom_ShearwaterBridge` is skipped.
5. Test EastScarp_Village west edge -> Town.
6. Confirm the Town X109 landing is walkable and does not bounce back.
7. If either direction fails, use `debug ppp` at the failed trigger/landing tile.
8. Send a fresh full SMAPI log if Content Patcher reports errors.

Only after both directions pass should TEST 2 be promoted to a stable UniqueID/release candidate and receive optional visual entrance treatment.

---

# Other open items

## Visual localization

The Chinese statement screens are baked PNG assets outside the JSON localization audit:

- `SDS.statement1.png`
- `SDS.statement2.png`
- `SDS.statement3.png`

A separate Vietnamese visual hotfix test exists. Keep it separate from the East Scarp compatibility pack.

## Portraits

SDS high-resolution portraits require Portraiture for correct display in the user's setup. The user has already moved the portrait assets there.

---

## Persistence rule

Every confirmed runtime result and compatibility patch must be committed before being considered complete. Update `CHECKPOINT.json`, this root handoff, and the current session handoff whenever runtime state changes.
