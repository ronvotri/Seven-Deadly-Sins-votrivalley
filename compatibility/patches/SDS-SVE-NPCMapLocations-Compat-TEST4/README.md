# SDS × SVE × NPC Map Locations Compatibility — TEST 4

TEST 3 exposed a bad artificial boundary:

- Town (79,53) -> Default
- Town (80,53) -> SDS_EastTown

Those tiles are only one step apart, but the minimap marker jumped from roughly runtime X765.75 to X864. The X80 split cut directly through a walkable bridge/path.

## Validated anchors

- Town 40,26: PASS under the old/default mapping.
- Town 38,58: lower-central area needs correction.
- Town 79,53 and 80,53: must be continuous.
- Joja area: east calibration is already good.
- SDS church: east calibration is already good.

## TEST 4 strategy

1. North-west / central: X0-79, Y0-39, preserving the validated mapping.
2. Lower west / central: X0-79, Y40-115, with a wider X projection that joins the east zone smoothly.
3. East Town: X80-172, Y0-115, keeping the validated Joja/church calibration.
4. Keep the Shearwater Bridge hard override.

Expected around Y53:

- Town X79 -> raw world-map X about 215.1
- Town X80 -> raw world-map X 216.0

So crossing one tile should move about one map pixel instead of the large TEST 3 jump.

## Install

Remove TEST 1, TEST 2, and TEST 3. Install only TEST 4 and restart Stardew Valley completely.

## Test order

1. Town 40,26.
2. Town 38,58 near Pierre / central area.
3. Walk slowly across X78 -> X79 -> X80 -> X81 around Y53.
4. Recheck Joja and church.
5. Recheck Custom_ShearwaterBridge.

Useful commands:

```text
debug WorldMapPosition true
debug ppp
```
