# Runtime Finding — Bridge route, minimap, and Portraiture

Date: 2026-09-12

## 1. East Scarp route behavior

Runtime testing after TEST 2 showed:

- the user can travel naturally from the main world through the railroad / Shearwater Bridge path into East Scarp;
- the user considers this forward route acceptable;
- TEST 2 overwrote EastScarp_Village west-edge return warps, so the reverse direction jumps directly from East Scarp to Town;
- this creates an asymmetric route and is visually/gameplay-wise undesirable.

### Decision

TEST 2 direct return is **rejected**.

Do not promote `SDS-SVE-EastScarp-DirectRoute-TEST2`.

Preferred route for the tested modpack is the existing SVE / East Scarp two-way bridge chain:

`main world / railroad -> Custom_ShearwaterBridge -> EastScarp_Village`

and the same path in reverse.

Immediate practical action: remove TEST 2 and re-test the native return route before creating any new warp patch.

## 2. Minimap / farmer marker

Installed runtime mod identified from the user's SMAPI setup:

- NPC Map Locations 3.5.2
- UniqueID: `Bouhm.NPCMapLocations`

The mod uses `Data/WorldMap` position data when available and derives custom-location placement from warp topology otherwise. SDS heavily changes Town topology while the final world-map position data can remain based on vanilla/SVE assumptions, so the farmer marker can appear at the wrong place on the world map/minimap.

Classification:

**separate map-coordinate compatibility issue, not a warp failure.**

Do not guess MapVectors. Build a dedicated NPC Map Locations compatibility patch only after obtaining/deriving correct Town map vectors for the final SDS+SVE Town layout.

## 3. SDS portraits / Portraiture

SDS 3.13.4 ships high-resolution portrait PNGs and explicitly lists Portraiture as the PC HD-portrait prerequisite in its included readme.

The raw SDS Content Patcher pack loads those PNGs directly into `Portraits/<NPC>`, which explains the oversized/cropped appearance when Portraiture is not actively using the SDS portrait set.

Recommended user-side configuration:

- keep the copied SDS portraits in `Mods/Portraiture/Portraits/Seven Deadly Sins/`;
- set Portraiture `config.json` active set to `Seven Deadly Sins` so it loads automatically;
- no repeated P-key switching should be required once that active set is saved.

Keep this separate from East Scarp route compatibility.
