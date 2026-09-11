# SDS × East Scarp × SVE Compatibility Research

> Research checkpoint created 2026-09-11. This document is the source of truth for the compatibility investigation. Do not treat hypotheses as confirmed conclusions.

## Goal

Determine whether **Seven Deadly Sins 3.13.4** can safely coexist with **East Scarp 3.0.9**, especially in a larger setup that also includes **Stardew Valley Expanded (SVE)**, and identify whether a compatibility patch is needed.

Target modpack context currently being considered:

- Seven Deadly Sins 3.13.4
- East Scarp 3.0.9
- Stardew Valley Expanded
- Ridgeside Village
- Pelipper Town and its optional compatibility packs
- StarCrossed

The immediate investigation is specifically **SDS ↔ East Scarp**, with SVE conditions taken into account.

---

## Inputs

### Seven Deadly Sins

- Version: **3.13.4**
- Nexus file ID: **178657**
- Existing repository contains the completed Vietnamese localization and audits, but not the complete original SDS map/assets.
- Exact original SDS map-related files were extracted from the same SMAPI dataset source used for the 3.13.4 localization audit.

Temporary extraction workflow:

- `.github/workflows/sds-extract-map-compat.yml`
- workflow trigger commit: `42977829ac9a7d65c1a14b5f0bf60db4df78e2ca`
- workflow run: `34609160529`
- result: **success**
- artifact name: `sds-3.13.4-map-compat-files`
- artifact ID: `10267372515`
- artifact size: `4,405,688 bytes`
- artifact digest: `sha256:9078e6128212727ad159c43cc62af69a5f4c1ffacf61add8bfd88e267d941c83`
- artifact expires: `2026-12-10T14:16:35Z`

The extraction is complete. The next step is to inspect its exact SDS map/content files before drawing final compatibility conclusions.

### East Scarp

User supplied the complete mod archive:

- archive: `East Scarp.rar`
- observed East Scarp version: **3.0.9**

The archive itself is not committed to this repository. Only compatibility findings are persisted here.

---

## Confirmed East Scarp findings so far

### 1. East Scarp patches vanilla `Maps/Town` when SVE is NOT installed

The relevant East Scarp Town integration uses:

- map patch asset: `assets/Patches/Town_ES.tmx`
- target: `Maps/Town`
- target area observed during inspection:
  - **X = 109**
  - **Y = 63**
  - **Width = 21**
  - **Height = 14**

This is the eastern/right-hand edge of Pelican Town, which matches the remembered conflict area.

### 2. East Scarp's vanilla-Town entrance includes warps around the eastern edge

Observed Town-side transition is around:

- **Town X ≈ 120**
- **Y ≈ 72–75**
- destination: **EastScarp_Crossing**

Exact warp tiles/properties should be re-checked against the extracted map/content before building a patch, but this establishes the conflict zone to compare against SDS.

### 3. East Scarp disables that vanilla `Maps/Town` patch when SVE is installed

The Town patch has a Content Patcher condition equivalent to:

```text
HasMod FlashShifter.StardewValleyExpandedCP = false
```

Therefore the common statement "East Scarp always occupies the east side of vanilla Town" is **not true when SVE is installed**.

This distinction is critical:

- **SDS + East Scarp without SVE** may collide directly in vanilla `Maps/Town`.
- **SDS + East Scarp + SVE** follows a different East Scarp connection route and must be analyzed separately.

### 4. With SVE present, East Scarp uses the Shearwater Bridge route

Observed SVE-aware route references:

```text
Custom_ShearwaterBridge
→ EastScarp_Village
```

This is encouraging because East Scarp no longer needs to inject its normal east-Pelican-Town entrance when SVE is present.

However, this does **not yet prove** SDS + East Scarp + SVE is conflict-free. SDS may still patch vanilla Town, SVE maps, shared warps, festival maps, schedules, or other locations.

---

## Important distinction: Pelipper compatibility files

Optional files such as:

- `PelipperTown.RidgesideVillage`
- `PelipperTown.SVE`
- `PelipperTown.EastScarp`
- `PelipperTown.StarCrossed`

are compatibility integrations for **Pelipper Town ↔ those expansions**.

They do **not** by themselves fix:

- Seven Deadly Sins ↔ East Scarp
- Seven Deadly Sins ↔ SVE

Do not mistake the Pelipper East Scarp optional file for an SDS/East Scarp compatibility patch.

---

## Current working hypotheses

These are NOT final conclusions yet.

### Case A: SDS + East Scarp, no SVE

**Risk: high enough to investigate directly.**

Reason: East Scarp explicitly modifies the east side of vanilla `Maps/Town`, exactly the broad area remembered as being relevant to SDS.

Need to compare the SDS 3.13.4 `Maps/Town` patch coordinates, patch mode, and warp edits against East Scarp's `X109 Y63 W21 H14` region.

### Case B: SDS + East Scarp + SVE

**Potentially safer than Case A.**

Reason: East Scarp disables its vanilla Town entrance and routes through SVE's Shearwater Bridge integration.

Still need to check:

- whether SDS patches the same SVE-adjusted Town region;
- whether SDS modifies SVE-relevant map assets or warps;
- whether any SDS custom location connects through tiles/warps that SVE replaces;
- festival/event map edits;
- NPC schedule destinations/warps.

### Case C: SDS + Ridgeside Village

No direct map collision has been established in this investigation yet. Treat as **not yet proven problematic**, but festival/schedule overlaps may still need runtime testing.

---

## Next technical steps

1. Download/open artifact `10267372515` (`sds-3.13.4-map-compat-files`).
2. Identify all SDS entries that target or edit:
   - `Maps/Town`
   - `Town`
   - `BusStop`
   - `Forest`
   - `Mountain`
   - `Railroad`
   - SVE-specific maps if any
   - warp/touch-action/map-property edits
3. Record SDS Town patch source map and exact `FromArea` / `ToArea` coordinates.
4. Overlay/compare SDS affected rectangles against East Scarp's vanilla Town rectangle:
   - East Scarp: `X109 Y63 W21 H14`
5. Compare warp destinations and tile properties around the eastern Town boundary.
6. Separately evaluate behavior with SVE installed, because East Scarp changes its integration path.
7. Classify final result as one of:
   - no patch required;
   - small warp/entrance compatibility patch;
   - map overlay compatibility patch required;
   - fundamentally incompatible without larger redesign.
8. If a patch is required, build it as a **separate compatibility mod**, not by modifying the localization files.

---

## Persistence rule for this investigation

Any confirmed compatibility finding or completed patch must be committed to GitHub before being treated as finished.

When continuing this investigation in another chat/session:

- do not restart the Vietnamese localization;
- do not re-investigate East Scarp from zero;
- start from this file;
- inspect artifact `10267372515` first;
- then compare exact SDS Town/map edits with the East Scarp findings above.

## Current resume point

**SDS 3.13.4 map extraction is complete and ready for inspection.**

The most important confirmed discovery so far is that **East Scarp's vanilla east-Town patch is conditional and is disabled when SVE is installed**, which means `SDS + East Scarp` and `SDS + East Scarp + SVE` must be treated as two distinct compatibility cases.
