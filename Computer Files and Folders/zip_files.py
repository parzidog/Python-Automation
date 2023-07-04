from pathlib import Path
from zipfile import ZipFile

# Create zip files

root_dir = Path("files")
archive_path = Path("archive.zip")

with ZipFile(archive_path, "w") as zf:
    for path in root_dir.rglob("*.txt"):
        zf.write(path)

# Extract zip files

root_dir = Path(".")
destination_path = Path("files")

for path in root_dir.rglob("*.zip"):
    with ZipFile(path, "r") as zf:
        zf.extractall(path=destination_path)
