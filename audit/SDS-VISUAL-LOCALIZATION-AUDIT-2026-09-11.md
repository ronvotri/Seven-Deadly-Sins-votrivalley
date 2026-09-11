# SDS 3.13.4 Embedded Visual Localization Audit — 2026-09-11

## Trigger

Runtime testing of the completed Vietnamese localization revealed untranslated Chinese copyright/disclaimer screens and oversized/cropped NPC portraits.

## Embedded Chinese disclaimer screens

Exact SDS 3.13.4 source was re-audited through the SMAPI dataset.

Temporary workflow:

`.github/workflows/tmp-sds-visual-assets-audit.yml`

Workflow run:

`34623985877`

Artifact:

- ID: `10273865403`
- name: `sds-3.13.4-visual-assets-audit`
- digest: `sha256:11973bea55a2d6e7160716630d03691e9021f9a98a545424ab2470e68d0f7f09`

The visible Chinese text is baked into three image assets rather than stored in normal CP/DLL translation strings:

- `[CP] Seven Deadly Sins/Maps/CG/SDS.statement1.png`
- `[CP] Seven Deadly Sins/Maps/CG/SDS.statement2.png`
- `[CP] Seven Deadly Sins/Maps/CG/SDS.statement3.png`

Each source image is 704 × 352.

The corresponding maps are loaded as `Custom_SDS.statement1`, `Custom_SDS.statement2`, and `Custom_SDS.statement3` during the SDS copyright/disclaimer event.

Therefore the previous 24,827/24,827 CP and 2,419/2,419 DLL text audits were accurate for text-localization coverage but did **not** cover text rasterized inside image assets. The release must not be described as visually 100% localized until these images are replaced/tested.

A Vietnamese replacement-image test hotfix was prepared locally for user runtime validation. It is not considered final until the user confirms all three screens render correctly in game.

## Oversized/cropped portraits

Exact SDS portrait source includes high-resolution assets, including:

- Raymond: 512 × 512
- Maria: 512 × 2816
- EdwardSDS: 512 × 768

These are not normal vanilla-resolution portrait sheets. When consumed through the vanilla portrait frame path, only a small portion of the HD image is visible, producing the observed forehead/hair crop.

Recommended runtime path is Portraiture-style HD portrait loading rather than destructive resizing of the SDS source art.

## Release implication

Localization status should now be interpreted as:

- CP text: complete
- DLL text: complete
- embedded image text: test fix pending runtime validation
- portrait display: installation/runtime integration issue, not a missing Vietnamese string
