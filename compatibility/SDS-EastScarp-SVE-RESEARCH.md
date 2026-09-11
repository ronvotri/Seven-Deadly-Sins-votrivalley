# SDS × East Scarp × SVE Compatibility Research

> Source-of-truth compatibility checkpoint. Confirmed findings are separated from provisional conclusions.

## Goal

Determine whether **Seven Deadly Sins 3.13.4** can coexist with **East Scarp 3.0.9**, especially in the intended larger modpack:

- Seven Deadly Sins 3.13.4
- East Scarp 3.0.9
- Stardew Valley Expanded (SVE)
- Ridgeside Village
- Pelipper Town + optional compatibility packs
- StarCrossed

The immediate problem is the eastern/right side of Pelican Town and the routes into East Scarp / SDS custom areas.

---

## Exact source inputs

### Seven Deadly Sins 3.13.4

- Nexus mod: `15100`
- Nexus file ID: `178657`
- Exact source extracted from SMAPI dataset.
- Workflow: `.github/workflows/sds-extract-map-compat.yml`
- Run: `34609160529`
- Result: **success**
- Artifact: `sds-3.13.4-map-compat-files`
- Artifact ID: `10267372515`
- Artifact digest: `sha256:9078e6128212727ad159c43cc62af69a5f4c1ffacf61add8bfd88e267d941c83`

### East Scarp 3.0.9

User supplied full `East Scarp.rar`.

A second exact extractor is also being run against the SMAPI dataset so the final comparison does not depend on local RAR tooling:

- workflow: `.github/workflows/tmp-eastscarp-3.0.9-extract.yml`
- trigger commit: `5ca602cd531f4bed7ead182d640a407a2c424253`
- run: `34614235814`
- desired source version: **3.0.9**

The Nexus/SMAPI metadata for East Scarp 3.0.9 explicitly says the mod is **likely not compatible with Seven Deadly Sins**, which matches the map conflict described below. That statement is treated as a warning, not as a technical explanation by itself.

---

# Confirmed SDS map behavior

## A. SDS WITHOUT SVE

SDS 3.13.4 does not merely add a few tiles to vanilla Town.

It has this logic in `assets/Data/MapWarps.json`:

```text
Action: Load
Target: Maps/Town
FromFile: Maps/SDS.Town.tmx
When: HasMod FlashShifter.StardewValleyExpandedCP = false
```

So when SVE is absent, SDS **replaces the entire Pelican Town map** with `Maps/SDS.Town.tmx`.

Exact SDS Town map size:

- Width: **173 tiles**
- Height: **110 tiles**

SDS also adds Town warps to its custom Avalia Forest:

```text
129 22 -> Custom_SDS.AvaliaForest 3 29
130 22 -> Custom_SDS.AvaliaForest 3 29
131 22 -> Custom_SDS.AvaliaForest 3 29
```

## B. SDS WITH SVE

SDS 3.13.4 contains substantial **built-in SVE compatibility**.

When `FlashShifter.StardewValleyExpandedCP` is installed, SDS does **not** load `Maps/SDS.Town.tmx` as the whole Town map. Instead it overlays SVE's Town using `Maps/Compatible/...` assets.

Important SVE-aware SDS Town patches include:

- `SDS.Town.Flowerstall.tmx` → `X0 Y53 W28 H27`
- `SDS.Town.Shop(.tmx/_Joja)` → `X22 Y39 W26 H16`
- `SDS.Town.Tree(.tmx/_Joja)` → `X50 Y37 W18 H15`
- `SDS.Town.Centertree(.tmx/_Joja)` → `X44 Y22 W8 H11`
- `SDS.Town.lemonade.tmx` → `X16 Y19 W5 H5`
- `SDS.Town.draw*` → around `X57 Y95`

Most importantly, the main right-side SDS/SVE patch is:

```text
Target: Maps/Town
ToArea: X110 Y0 W63 H116
Priority: Late
When: SVE installed
```

There are three state variants of that same rectangle:

- `SDS.Town.Main.tmx`
- `SDS.Town.Main_Joja_Morris.tmx`
- `SDS.Town.Main_Joja.tmx`

Each source patch is exactly **63 × 116 tiles** and contains thousands of non-empty map tiles, so this is a major structural addition rather than a cosmetic patch.

SDS also adds, under SVE:

```text
129 22 -> Custom_SDS.AvaliaForest 3 29
130 22 -> Custom_SDS.AvaliaForest 3 29
131 22 -> Custom_SDS.AvaliaForest 3 29
```

Additional SVE-specific edits include a Morris property warp and removal/replacement of selected Town day/night tiles.

### Critical search result

A full text scan of the extracted SDS 3.13.4 source found **no references** to:

- `EastScarp`
- `EastScarp_Village`
- `ScarpCrossing`
- `Shearwater`
- `Custom_ShearwaterBridge`

So SDS itself does not appear to patch or depend on East Scarp's SVE bridge route.

---

# Confirmed East Scarp findings

## 1. East Scarp without SVE patches vanilla `Maps/Town`

Observed East Scarp 3.0.9 Town entrance integration:

- patch asset: `assets/Patches/Town_ES.tmx`
- target: `Maps/Town`
- ToArea:
  - **X = 109**
  - **Y = 63**
  - **Width = 21**
  - **Height = 14**

Town-side transition is around:

- X ≈ 120
- Y ≈ 72–75
- destination: `EastScarp_Crossing`

## 2. East Scarp disables that vanilla Town entrance when SVE is present

The Town integration has a condition equivalent to:

```text
HasMod FlashShifter.StardewValleyExpandedCP = false
```

Therefore `SDS + East Scarp` and `SDS + East Scarp + SVE` are technically different cases.

## 3. East Scarp's SVE-aware route uses Shearwater Bridge

Observed SVE-aware route:

```text
Custom_ShearwaterBridge -> EastScarp_Village
```

The exact East Scarp 3.0.9 extractor is being used to verify every relevant 3.0.9 patch before this case is marked fully clean.

---

# Direct overlap test: East Scarp rectangle vs SDS Town

East Scarp vanilla Town rectangle:

```text
X109..129
Y63..76
21 × 14 = 294 tiles
```

That exact rectangle was sampled from **SDS 3.13.4 `Maps/SDS.Town.tmx`**.

Occupancy inside those 294 tiles:

- `Back`: **294 / 294** non-empty
- `Buildings`: **222 / 294** non-empty
- `Front`: **111 / 294** non-empty
- `AlwaysFront`: **112 / 294** non-empty
- plus smaller Back2 / Paths content

This is decisive: the East Scarp entrance is **not landing on empty SDS terrain**. It cuts directly through a densely built part of SDS Town.

---

# Compatibility classification

## Case A: SDS 3.13.4 + East Scarp 3.0.9, NO SVE

### Status: 🔴 CONFIRMED HARD MAP CONFLICT

Reasons:

1. SDS replaces the full `Maps/Town` with `SDS.Town.tmx`.
2. East Scarp edits the eastern Town rectangle `X109 Y63 W21 H14`.
3. That rectangle is heavily occupied by SDS Buildings/Front/AlwaysFront content.
4. Load/edit order can therefore either:
   - overwrite part of SDS's built Town;
   - erase East Scarp's entrance;
   - produce broken collision/tile properties;
   - or leave inaccessible/bad warps depending on patch order.

This is no longer a hypothesis.

### Patch requirement

A compatibility patch is required if the user wants to run **SDS + East Scarp without SVE**.

The likely clean solution is **not** to preserve East Scarp's vanilla east-Town entrance in the same rectangle. Instead, move/re-route East Scarp's entrance to a safe connection or create a dedicated compatibility transition map.

---

## Case B: SDS 3.13.4 + East Scarp 3.0.9 + SVE

### Status: 🟢/🟡 DIRECT TOWN CONFLICT APPEARS AVOIDED, FINAL 3.0.9 AUDIT IN PROGRESS

Evidence so far:

1. SDS detects SVE and switches to its own SVE-compatible Town overlays.
2. East Scarp detects SVE and disables its normal vanilla east-Town entrance.
3. East Scarp instead connects through `Custom_ShearwaterBridge`.
4. SDS 3.13.4 contains **zero** references to East Scarp / ScarpCrossing / Shearwater Bridge.
5. SDS's SVE Town warp to Avalia Forest is at `X129–131, Y22`, far from East Scarp's old vanilla entrance around `Y72–75`.

This strongly suggests the user's intended combination **SDS + East Scarp + SVE** may avoid the specific hard collision that makes the no-SVE setup incompatible.

Still to verify from exact East Scarp 3.0.9 source:

- every `Maps/Town` patch condition;
- every `Maps/Custom_ShearwaterBridge` patch;
- any SVE-specific ScarpCrossing map load/edit;
- whether East Scarp 3.0.9 patches any other SDS/SVE location that SDS also modifies.

Do not call this fully green until that exact 3.0.9 source comparison is complete.

---

## Case C: SDS + Ridgeside Village

No direct map collision has been established in this investigation. Runtime festival/schedule overlap is still possible, but no equivalent hard Town-map conflict has been found yet.

---

# Pelipper compatibility files

These optional packs:

- `PelipperTown.RidgesideVillage`
- `PelipperTown.SVE`
- `PelipperTown.EastScarp`
- `PelipperTown.StarCrossed`

only integrate **Pelipper Town ↔ each expansion**.

They do not repair the SDS/East Scarp collision described above.

---

# Next technical steps

1. Let exact East Scarp 3.0.9 extractor run `34614235814` finish.
2. Inspect its exact `content.json`, `OtherMaps.json`, `SVE.json`, `Town_ES.tmx`, Shearwater/ScarpCrossing files.
3. Enumerate every East Scarp 3.0.9 target touching:
   - `Maps/Town`
   - `Maps/Custom_ShearwaterBridge`
   - SVE connection maps
4. Compare those targets against exact SDS 3.13.4 target list.
5. Finalize Case B classification.
6. If the user wants support for the **no-SVE** case, design a separate compatibility mod that reroutes East Scarp instead of overwriting SDS Town.
7. If the user is definitely installing SVE, prioritize a minimal SVE-aware compatibility guard only if the exact audit finds a remaining overlap.

---

## Persistence rule

All confirmed compatibility findings and any compatibility patch must be committed to GitHub before being counted as complete.

## Current resume point

**SDS side is fully inspected. Exact East Scarp 3.0.9 extraction is running.**

Do not restart localization or repeat SDS map analysis. Next session should inspect run `34614235814` / artifact from `.github/workflows/tmp-eastscarp-3.0.9-extract.yml`, then finish the SVE-aware comparison.
