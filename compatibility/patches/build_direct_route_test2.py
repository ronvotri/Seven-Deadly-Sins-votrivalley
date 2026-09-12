from __future__ import annotations

import json
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "compatibility" / "patches" / "SDS-SVE-EastScarp-DirectRoute-TEST2"
DIST = ROOT / "dist" / "compatibility"
PACK_NAME = "[CP] SDS-SVE-EastScarp-DirectRoute-TEST2"
OUTPUT = DIST / "SDS-SVE-EastScarp-DirectRoute-TEST2.zip"


def validate_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    manifest_path = SOURCE / "manifest.json"
    content_path = SOURCE / "content.json"
    readme_path = SOURCE / "README.md"

    for required in (manifest_path, content_path, readme_path):
        if not required.exists():
            raise FileNotFoundError(required)

    manifest = validate_json(manifest_path)
    content = validate_json(content_path)

    if manifest.get("UniqueID") != "VotriValley.SDS.SVE.EastScarp.DirectRouteTest2":
        raise ValueError("Unexpected TEST 2 UniqueID")

    changes = content.get("Changes", [])
    if len(changes) != 2:
        raise ValueError("Expected exactly two EditMap changes")

    town = changes[0]
    scarp = changes[1]
    if town.get("Target") != "Maps/Town":
        raise ValueError("First patch must target Maps/Town")
    if scarp.get("Target") != "Maps/EastScarp_Village":
        raise ValueError("Second patch must target Maps/EastScarp_Village")

    expected_town = {
        "110 72 EastScarp_Village 1 71",
        "110 73 EastScarp_Village 1 72",
        "110 74 EastScarp_Village 1 73",
    }
    if set(town.get("AddWarps", [])) != expected_town:
        raise ValueError("Unexpected Town direct-route warp set")

    expected_return = {
        "0 70 Town 109 72",
        "0 71 Town 109 72",
        "0 72 Town 109 73",
        "0 73 Town 109 74",
        "0 74 Town 109 74",
    }
    if set(scarp.get("AddWarps", [])) != expected_return:
        raise ValueError("Unexpected East Scarp return warp set")

    DIST.mkdir(parents=True, exist_ok=True)
    if OUTPUT.exists():
        OUTPUT.unlink()

    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for source in (manifest_path, content_path, readme_path):
            archive.write(source, Path(PACK_NAME) / source.name)

    with zipfile.ZipFile(OUTPUT, "r") as archive:
        names = set(archive.namelist())
        expected_names = {
            f"{PACK_NAME}/manifest.json",
            f"{PACK_NAME}/content.json",
            f"{PACK_NAME}/README.md",
        }
        if names != expected_names:
            raise ValueError(f"Unexpected archive contents: {sorted(names)}")

    print(f"Built {OUTPUT.relative_to(ROOT)}")
    print("Preflight: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
