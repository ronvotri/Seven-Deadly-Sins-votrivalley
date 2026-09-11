# Session Handoff — 2026-09-11

This file closes the SDS compatibility map-research phase and remains the first read for continuation sessions.

## Repository

`ronvotri/Seven-Deadly-Sins-votrivalley`

## Localization status

Seven Deadly Sins 3.13.4 Vietnamese localization is finished and must not be restarted.

- CP: 24,827 / 24,827, clean audit
- DLL: 2,419 / 2,419, clean audit
- release-ready localization ZIP already built
- canonical compatibility research file: `compatibility/SDS-EastScarp-SVE-RESEARCH.md`

## User's intended modpack context

The user wants to play a large combined Stardew Valley setup centered on:

- Seven Deadly Sins 3.13.4
- Stardew Valley Expanded
- East Scarp 3.0.9
- Ridgeside Village
- Pelipper Town
- PelipperTown.SVE
- PelipperTown.EastScarp
- PelipperTown.RidgesideVillage
- PelipperTown.StarCrossed when StarCrossed is installed

The user specifically remembered a map conflict on the right/east side of Pelican Town and asked whether East Scarp was the problematic mod.

## Exact source material used in the completed map audit

### SDS 3.13.4

Exact SDS 3.13.4 map-related source was extracted from Nexus file `178657` via the SMAPI dataset.

- workflow: `.github/workflows/sds-extract-map-compat.yml`
- run: `34609160529`
- artifact ID: `10267372515`
- artifact digest: `sha256:9078e6128212727ad159c43cc62af69a5f4c1ffacf61add8bfd88e267d941c83`

### East Scarp 3.0.9

The user uploaded the complete archive `East Scarp.rar`.

Exact East Scarp Core 3.0.9 files were extracted locally and inspected, including:

- `manifest.json`
- `content.json`
- `assets/Data/OtherMaps.json`
- `assets/Data/SVE.json`
- `assets/Data/LocationData.json`
- `assets/Data/ShortCutWarps.json`
- `assets/Data/WarpNetwork.json`
- `assets/Patches/Town_ES.tmx`
- `assets/Patches/ES_ShearwaterBridgeStrip.tmx`
- `assets/Locations/Outdoors/ScarpCrossing_ESR.tmx`
- `assets/Locations/Outdoors/ScarpCrossing_SVE.tmx`

A temporary extractor against the SMAPI dataset was attempted for exact East Scarp 3.0.9 unpacked files:

- workflow: `.github/workflows/tmp-eastscarp-3.0.9-extract.yml`
- run: `34614235814`
- result: failed because the export did not expose the current unpacked 3.0.9 core under Nexus 5787

This failure is not a blocker because the user-supplied 3.0.9 archive was successfully inspected directly.

## Final map-level findings

### Case A: SDS 3.13.4 + East Scarp 3.0.9 WITHOUT SVE

**CONFIRMED HARD MAP CONFLICT.**

East Scarp patches vanilla Town at:

`X109 Y63 W21 H14`

and adds Town-side warps around:

`X120 Y72-75 -> EastScarp_Crossing`

SDS without SVE replaces the entire Pelican Town map with `Maps/SDS.Town.tmx`.

Inside the exact East Scarp rectangle on SDS Town:

- Back: 294 / 294 occupied
- Buildings: 222 / 294 occupied
- Front: 111 / 294 occupied
- AlwaysFront: 112 / 294 occupied

Therefore East Scarp's normal east-Town entrance slices through a densely constructed SDS area.

**Conclusion:** do not run SDS + East Scarp without SVE unless a dedicated reroute compatibility patch is built.

### Case B: SDS 3.13.4 + East Scarp 3.0.9 + SVE

**MAP-LEVEL COMPATIBLE IN THE AUDITED ROUTE. Runtime validation is still required.**

When SVE is installed, East Scarp disables `Town_ES.tmx` and instead uses the SVE-aware Shearwater route.

SVE Town outgoing warp strip:

`Town X119,Y72-76 -> Custom_ShearwaterBridge`

East Scarp bridge return:

`Custom_ShearwaterBridge -> Town 118,72`

East Scarp then connects the bridge onward to `EastScarp_Village`.

SDS with SVE uses a major `Priority: Late` Town patch at:

`X110 Y0 W63 H116`

Three SDS main variants were checked:

- `SDS.Town.Main.tmx`
- `SDS.Town.Main_Joja_Morris.tmx`
- `SDS.Town.Main_Joja.tmx`

For all three:

- `Town 118,72` remains walkable
- `Town 119,72-76` remains walkable
- the critical strip has no Buildings / Buildings2 / Buildings7 blockers
- a walkable route from the bridge strip back into the rest of Town remains
- SDS does not target `Custom_ShearwaterBridge`
- SDS does not target `EastScarp_Village` or `EastScarp_Crossing`
- SDS does not provide a replacement Town `Warp` map-property key in the main overlay

Other East Scarp SVE-aware edits also did not geometrically overlap the relevant SDS patches:

- East Scarp Town quest/garden edits around X59-68, Y13-20
- East Scarp Mountain patch X86 Y35 W9 H6

**Conclusion:** do not create a pre-emptive SDS/East Scarp map patch for the intended SVE setup. Test in game first.

## Pelipper optional compatibility files

The following are Pelipper integrations only:

- `PelipperTown.RidgesideVillage`
- `PelipperTown.SVE`
- `PelipperTown.EastScarp`
- `PelipperTown.StarCrossed`

They do not solve SDS/East Scarp conflicts by themselves.

For the user's intended setup, install the corresponding Pelipper compatibility packs for every expansion actually present.

## Runtime-validation framework added in continuation

A concrete runtime matrix now exists at:

`compatibility/RUNTIME-VALIDATION-CHECKLIST.md`

Checklist commit:

`3bc0be9f50b01f9586f715ac16068822ab344577`

Checkpoint was advanced to runtime-validation-ready state in:

`045aca0cf23e9664d5bbd3760559a2ed1756618e`

The checklist covers:

- clean SMAPI boot / dependency / Content Patcher errors;
- Town -> Custom_ShearwaterBridge -> EastScarp_Village and return;
- SDS Avalia Forest access;
- Pelipper integration sanity checks;
- Ridgeside Village travel sanity checks;
- NPC schedule/pathfinding checks;
- festival validation;
- failure classification and minimal-patch policy.

No runtime compatibility result has been invented or claimed without an actual test run.

## What NOT to do next

- Do not resume Vietnamese translation.
- Do not repeat the SDS map extraction.
- Do not re-investigate the East Scarp Town rectangle from zero.
- Do not create a compatibility patch for the SVE case without a reproduced runtime issue.
- Do not label a Pelipper or RSV failure as an SDS conflict until SDS involvement is evidenced.

## Exact next action

The next phase is **runtime compatibility validation**.

1. Launch the intended full modpack and load a save.
2. Exercise both directions of `Town -> Custom_ShearwaterBridge -> EastScarp_Village`.
3. Capture a fresh complete SMAPI log from the same run.
4. Inspect Content Patcher warnings, duplicate map edits, missing dependencies, schedule/path errors, festival errors, and load-order issues.
5. Verify SDS Avalia Forest access still works.
6. Sanity-test RSV travel and every installed Pelipper compatibility route.
7. Only if a concrete reproducible runtime problem appears, build the smallest targeted compatibility patch.

If the user specifically wants a setup without SVE later, that is already a proven incompatible case and should go straight to designing a dedicated East Scarp reroute compatibility mod.

## Source-of-truth files for next continuation

Read these first:

1. `compatibility/SESSION-2026-09-11-HANDOFF.md`
2. `compatibility/RUNTIME-VALIDATION-CHECKLIST.md`
3. `compatibility/SDS-EastScarp-SVE-RESEARCH.md`
4. `CHECKPOINT.json`
5. `HANDOFF.md`

## Persistence rule

Every confirmed finding, runtime fix, or compatibility patch must be committed to GitHub before it is considered complete. End each future session by updating the compatibility research/checkpoint/handoff files.
