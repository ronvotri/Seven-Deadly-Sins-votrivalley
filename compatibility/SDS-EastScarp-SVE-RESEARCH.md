# SDS × East Scarp × SVE Compatibility Research

> Source-of-truth compatibility checkpoint. **Map-level investigation is now complete for the tested versions.** Runtime festival/schedule/event testing is still recommended before calling the entire mod combination universally compatible.

## Target setup

User is considering a large modpack containing:

- Seven Deadly Sins **3.13.4**
- East Scarp **3.0.9**
- Stardew Valley Expanded (SVE)
- Ridgeside Village
- Pelipper Town + optional compatibility packs
- StarCrossed

The main question investigated here is the eastern/right side of Pelican Town and the route into East Scarp.

---

# Exact source inputs

## Seven Deadly Sins 3.13.4

- Nexus mod: `15100`
- Nexus file ID: `178657`
- Exact source extracted from SMAPI dataset.
- Workflow: `.github/workflows/sds-extract-map-compat.yml`
- Run: `34609160529`
- Result: **success**
- Artifact: `sds-3.13.4-map-compat-files`
- Artifact ID: `10267372515`
- Artifact digest: `sha256:9078e6128212727ad159c43cc62af69a5f4c1ffacf61add8bfd88e267d941c83`

## East Scarp 3.0.9

User supplied the complete `East Scarp.rar`.

Exact core files were successfully extracted locally from that archive using libarchive, including:

- `East Scarp Core/manifest.json`
- `East Scarp Core/content.json`
- `East Scarp Core/assets/Data/OtherMaps.json`
- `East Scarp Core/assets/Data/SVE.json`
- `East Scarp Core/assets/Data/LocationData.json`
- `East Scarp Core/assets/Data/ShortCutWarps.json`
- `East Scarp Core/assets/Data/WarpNetwork.json`
- `East Scarp Core/assets/Patches/Town_ES.tmx`
- `East Scarp Core/assets/Patches/ES_ShearwaterBridgeStrip.tmx`
- `East Scarp Core/assets/Locations/Outdoors/ScarpCrossing_ESR.tmx`
- `East Scarp Core/assets/Locations/Outdoors/ScarpCrossing_SVE.tmx`

Manifest confirms:

- Name: `East Scarp: Locations`
- Version: **3.0.9**
- UniqueID: `Lemurkat.EastScarp`
- optional SVE dependency: `FlashShifter.StardewValleyExpandedCP`

The manifest also still lists an old optional SDS-family dependency `ricehit.SDSMAPS`; current SDS 3.13.4 uses `ricehit.SevenDeadlySinsCP`, so this old dependency should not be assumed to provide modern SDS compatibility or load ordering.

A temporary SMAPI-dataset extractor for East Scarp was also attempted:

- workflow: `.github/workflows/tmp-eastscarp-3.0.9-extract.yml`
- run: `34614235814`
- result: **failure** because the dataset export did not expose an unpacked 3.0.9 core under Nexus 5787.

This does not block the research because the exact user-supplied 3.0.9 RAR was successfully extracted locally.

---

# Case A: SDS + East Scarp WITHOUT SVE

## 🔴 Status: CONFIRMED HARD MAP CONFLICT

### SDS behavior

Without SVE, SDS 3.13.4 loads:

```text
Action: Load
Target: Maps/Town
FromFile: Maps/SDS.Town.tmx
When: SVE = false
```

So SDS replaces the entire Pelican Town map.

Exact SDS Town dimensions:

- **173 × 110 tiles**

### East Scarp behavior

Without SVE, East Scarp 3.0.9 patches:

```text
Target: Maps/Town
FromFile: assets/Patches/Town_ES.tmx
ToArea: X109 Y63 W21 H14
When: SVE = false
```

It also appends Town warps:

```text
120 72 -> EastScarp_Crossing
120 73 -> EastScarp_Crossing
120 74 -> EastScarp_Crossing
120 75 -> EastScarp_Crossing
```

### Exact overlap test

East Scarp rectangle:

```text
X109..129
Y63..76
21 × 14 = 294 tiles
```

Occupancy in exact SDS `Maps/SDS.Town.tmx` across those 294 tiles:

- Back: **294 / 294**
- Buildings: **222 / 294**
- Front: **111 / 294**
- AlwaysFront: **112 / 294**
- plus smaller Back2 / Paths content

This is not empty terrain. East Scarp cuts directly through a heavily built SDS Town region.

### Conclusion

**SDS + East Scarp without SVE requires a compatibility patch.**

A clean solution should reroute East Scarp instead of forcing `Town_ES.tmx` into the same SDS structure.

---

# Case B: SDS + East Scarp + SVE

## 🟢 Status: NO HARD MAP COLLISION FOUND IN THE EAST SCARP ROUTE

This case behaves very differently from Case A.

## 1. East Scarp disables its vanilla Town entrance

Exact East Scarp 3.0.9:

```text
Town_ES.tmx -> Maps/Town X109 Y63 W21 H14
When: SVE = false
```

Therefore the destructive no-SVE Town overlay does **not** run when SVE is installed.

## 2. East Scarp switches to SVE's Shearwater Bridge

Exact `assets/Data/SVE.json`:

East Scarp patches:

```text
Maps/Custom_ShearwaterBridge
FromFile: assets/Patches/ES_ShearwaterBridgeStrip.tmx
ToArea: X59 Y14 W1 H12
```

Bridge map Warp property becomes:

```text
west edge y19..23 -> Town 118 72
x60 y19..23 -> EastScarp_Village y70..74
```

East Scarp Village also gets corresponding warps to `Custom_ShearwaterBridge`.

## 3. SVE's actual Town exit is X119, Y72–76

Current upstream SVE Town map defines:

```text
119 72 -> Custom_ShearwaterBridge 0 20
119 73 -> Custom_ShearwaterBridge 0 20
119 74 -> Custom_ShearwaterBridge 0 20
119 75 -> Custom_ShearwaterBridge 0 20
119 76 -> Custom_ShearwaterBridge 0 20
```

So the route expected by East Scarp is:

```text
Town X119,Y72–76
↔ Custom_ShearwaterBridge
↔ EastScarp_Village
```

with return landing at `Town 118,72`.

## 4. SDS does patch over that area, but the route remains walkable

With SVE installed, SDS uses a large `Priority: Late` patch:

```text
Target: Maps/Town
ToArea: X110 Y0 W63 H116
```

Variants:

- `SDS.Town.Main.tmx`
- `SDS.Town.Main_Joja_Morris.tmx`
- `SDS.Town.Main_Joja.tmx`

This includes the SVE bridge entrance coordinates.

However, exact tile inspection shows the critical strip stays walkable in **all three SDS variants**:

### Town 118,72

- has Back tile
- no Buildings / Buildings2 / Buildings7 collision tile

### Town 119,72–76

All five outgoing SVE warp tiles have a Back tile and **no Buildings-layer blocker** in all three SDS state variants.

Examples in normal `SDS.Town.Main.tmx`:

```text
119,72: Back + decorative AlwaysFront, no Buildings
119,73: Back + decorative AlwaysFront, no Buildings
119,74: Back only
119,75: Back only
119,76: Back only
```

The grass/floor Back tiles used there have no blocking property.

A walkability graph using Back-present + no-Buildings as the passability rule found a continuous route from `Town 119,72` back to the western edge of SDS's main patch in **all three SDS variants**.

Therefore SDS changes the visuals/terrain in this region, but does not wall off the Shearwater warp strip.

## 5. The SVE Warp map property should survive SDS's tile overlay

SDS's `SDS.Town.Main*` source maps contain no replacement `Warp` map property.

The SDS patch edits tiles and separately uses `AddWarps` for its own Avalia Forest connection; it does not replace SVE's existing Town Warp property.

Content Patcher's `EditMap` default map patch mode is `ReplaceByLayer`, which replaces tile layers in the patched rectangle, not unrelated map-property keys that aren't supplied by the source patch.

So SVE's Town warp entries at X119,Y72–76 are expected to remain after the SDS tile patch.

## 6. Other East Scarp SVE-aware Town edits do not overlap SDS Town additions

Exact East Scarp 3.0.9 SVE-related Town edits include:

- Aideen garden area: roughly `X59 Y13 W10 H8`
- single quest tile: `X66 Y17`
- several Paths removals around X59/X65, Y15–20

Relevant SDS SVE patches are elsewhere:

- Center tree: `X44 Y22 W8 H11`
- Tree: `X50 Y37 W18 H15`
- Shop: `X22 Y39 W26 H16`
- Main right side: `X110 Y0 W63 H116`

No geometric overlap was found between East Scarp's Aideen/quest Town edits and SDS's nearby SVE patches.

## 7. Mountain edits also do not overlap

East Scarp SVE Mountain patch:

```text
X86 Y35 W9 H6
```

SDS SVE Mountain road patch:

```text
X41 Y0 W6 H6
```

Other SDS Mountain changes are around the far-left mine entrance. No overlap with East Scarp's SVE Mountain patch was found.

## 8. SDS does not edit Shearwater Bridge itself

Full exact SDS 3.13.4 source scan found zero references to:

- `EastScarp`
- `EastScarp_Village`
- `EastScarp_Crossing`
- `ScarpCrossing`
- `Shearwater`
- `Custom_ShearwaterBridge`

So East Scarp's bridge/location maps are not directly overwritten by SDS.

### Map-level conclusion for SVE setup

For **SDS 3.13.4 + East Scarp 3.0.9 + SVE**, the specific hard map conflict seen without SVE is avoided.

The East Scarp route through Shearwater Bridge appears **functionally preserved at the map/warp layer**.

### Important scope limit

This does **not** prove universal full-mod compatibility. Remaining possible issues include:

- festival maps / festival NPC placement;
- NPC schedules or pathfinding during special days;
- event conditions and shared vanilla locations;
- third-party East Scarp addons;
- interactions introduced by other large mods in the user's pack.

Therefore the practical classification is:

**🟢 MAP-LEVEL COMPATIBLE WITH SVE, RUNTIME VALIDATION RECOMMENDED.**

No compatibility patch should be created for the SVE case unless actual gameplay/SMAPI testing reveals a remaining problem.

---

# Case C: SDS + Ridgeside Village

No equivalent hard map collision has been established in this investigation.

Runtime festival/schedule testing is still recommended, especially in a large combined expansion pack.

---

# Pelipper compatibility files

These optional packs:

- `PelipperTown.RidgesideVillage`
- `PelipperTown.SVE`
- `PelipperTown.EastScarp`
- `PelipperTown.StarCrossed`

integrate **Pelipper Town ↔ each listed expansion**.

They do not repair the no-SVE SDS/East Scarp collision, and they are not a substitute for SDS compatibility analysis.

For the user's intended SVE setup, install the corresponding Pelipper compatibility files for each expansion being used.

---

# Practical recommendation

For this specific modpack, prefer:

```text
SDS 3.13.4
+ SVE
+ East Scarp 3.0.9
+ Ridgeside Village
+ Pelipper Town
+ Pelipper compatibility packs for SVE / East Scarp / RSV / StarCrossed as applicable
```

Do **not** use `SDS + East Scarp` without SVE unless a dedicated reroute compatibility patch is added.

For the SVE setup, first test without an extra SDS/East Scarp patch. If gameplay reveals a broken route or map issue, capture the SMAPI log and exact location; then make the smallest targeted patch instead of pre-emptively modifying maps that already appear compatible.

---

## Persistence rule

All confirmed compatibility findings and any future compatibility patch must be committed to GitHub before being counted as complete.

## Current resume point

**Map-level SDS × East Scarp × SVE investigation is complete.**

Next valid work:

1. runtime-test the intended modpack;
2. inspect SMAPI warnings/conflicts;
3. test Town → Shearwater Bridge → East Scarp in game;
4. test important festivals and NPC schedules;
5. only build a compatibility patch if a concrete runtime problem is reproduced.
