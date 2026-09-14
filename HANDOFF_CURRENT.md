# CURRENT HANDOFF — Seven Deadly Sins 3.13.4

Read first:

1. `compatibility/SESSION-2026-09-15-HANDOFF.md`
2. `CHECKPOINT.json`
3. `HANDOFF.md`

Current state:

- Vietnamese text localization is complete: CP 24,827/24,827; DLL 2,419/2,419.
- Portraiture issue: temporarily accepted/OK. Do not reopen unless requested.
- 3 Vietnamese statement PNGs: temporarily accepted/OK and merged with localization in the preferred session package.
- Native SVE/East Scarp route is preferred: `main world / railroad <-> Custom_ShearwaterBridge <-> EastScarp_Village`.
- DirectRoute TEST2 is rejected for normal use.
- Deep Shearwater minimap debugging was stopped by user.
- Current practical minimap solution is `SDS-SVE-NPCMapLocations-Compat-LITE`, which fixes Town only and intentionally leaves `Custom_ShearwaterBridge` untouched.
- Old minimap TEST1-TEST8 are historical only, not release candidates.
- There is no mandatory open bug. Follow the user's next request.

LITE source:

`compatibility/patches/SDS-SVE-NPCMapLocations-Compat-LITE/`

LITE builder:

`compatibility/patches/build_npcmap_compat_lite.py`

Do not restart translation or Shearwater research automatically.
