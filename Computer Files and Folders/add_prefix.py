from pathlib import Path
import time

root_dir = Path("files")
file_paths = root_dir.iterdir()

# Add text in file name

for path in file_paths:
    new_filename = "new-" + path.stem + path.suffix
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)

# Pause to see changes

time.sleep(5)

# Remove text in file name

root_dir = Path("files")
file_paths = root_dir.iterdir()

name = ""

for path in file_paths:
    file_name = path.stem.split("-")
    file_name.remove("new")
    for f in file_name:
        name += f
    new_filename = f + path.suffix
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)
