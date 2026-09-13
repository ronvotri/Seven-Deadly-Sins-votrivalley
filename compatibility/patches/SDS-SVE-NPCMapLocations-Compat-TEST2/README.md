# SDS × SVE × NPC Map Locations Compatibility — TEST 2

Purpose
-------
Fix world-map / minimap farmer marker alignment when using:
- Seven Deadly Sins 3.13.4
- Stardew Valley Expanded
- NPC Map Locations 3.5.2

TEST 1 status
-------------
Town calibration appears correct in runtime testing.

New TEST 2 fix
--------------
SVE already defines Custom_ShearwaterBridge in Data/WorldMap at:
X250 Y90 Width43 Height10

That coordinate was designed for SVE's map artwork. SDS replaces the world map
artwork, and on the SDS map that same coordinate visually overlaps the church.

TEST 2 keeps the working Town calibration and moves the Shearwater Bridge marker to:
X286 Y101 Width13 Height7

This places it along the far-eastern coast of the SDS world map instead of the church.

Install
-------
IMPORTANT: remove TEST 1 first.

Delete:
[CP] SDS-SVE-NPCMapLocations-Compat-TEST1

Then install:
[CP] SDS-SVE-NPCMapLocations-Compat-TEST2

Restart Stardew Valley completely.

Test
----
1. Confirm Town / Joja / church marker still looks correct.
2. Enter Custom_ShearwaterBridge.
3. Confirm the farmer marker moves to the east edge/coast instead of the church.
4. Continue into East Scarp and return through the bridge.

If the bridge marker is only slightly off, send a screenshot and we can fine-tune
X/Y without changing the working Town calibration.
