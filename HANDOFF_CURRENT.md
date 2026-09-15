# CURRENT HANDOFF — Seven Deadly Sins 3.13.4

Read first:

1. `compatibility/SESSION-2026-09-15-HANDOFF.md`
2. `CHECKPOINT.json`
3. `HANDOFF.md`
4. `audit/NAME_ITEM_AUDIT_2026-09-15.md`

Current state:

- Vietnamese text localization remains complete: CP **24,827/24,827**; DLL **2,419/2,419**.
- A full proper-name/item consistency audit was completed on 2026-09-15 after a concrete user report.
- Audited changes: **1,262 CP keys + 195 DLL keys**, with **0 control-token mismatches** and **0 known bad aliases remaining**.
- Canonical English character spellings are locked for names such as `Sariel`, `Lane`, `Rane`, `Pelette`, `Garnet`, `Regla`, `Teresa`, `Theodor`, `Coffey`, `Xenia`, `Siren`, `Lucas`, and `Five Songs`.
- Do not restore old forms such as `Shirai`, `Baibai`, `Ryan`, `Rhein`, `Pellet`, `Garrett`, `Rigela`, `Theresa`, `Theodore`, `Kofi`, or `Zinnia` when they represent those characters.
- Current audited session ZIP: `SDS-3.13.4-Vietnamese-Name-Item-Audit-Fix.zip`, SHA256 `7554385561307026b4674fbf01b4fe1640bad1fd4f1af3cc45e1616b6f264b54`.
- Audit record commit: `30db501c10048243cbc8187ac07fae0659b8dcd2`.
- Note: the repository's large release `vi.json` blobs have not yet been rebuilt from this audit. The audited session artifact is the preferred text-localization package until an explicit release rebuild is done.
- Portraiture issue: temporarily accepted/OK. Do not reopen unless requested.
- 3 Vietnamese statement PNGs: temporarily accepted/OK.
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

Do not restart translation, reintroduce pre-audit name aliases, or resume Shearwater research automatically.
