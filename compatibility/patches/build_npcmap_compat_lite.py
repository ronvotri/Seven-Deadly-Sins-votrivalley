from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "SDS-SVE-NPCMapLocations-Compat-LITE"
OUT = ROOT.parent.parent / "dist" / "compatibility" / "SDS-SVE-NPCMapLocations-Compat-LITE.zip"
PACK_NAME = "[CP] SDS-SVE-NPCMapLocations-Compat-LITE"

OUT.parent.mkdir(parents=True, exist_ok=True)

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for src in ("manifest.json", "content.json", "README.md"):
        path = SOURCE / src
        z.write(path, Path(PACK_NAME) / ("README-VI.txt" if src == "README.md" else src))

print(OUT)
