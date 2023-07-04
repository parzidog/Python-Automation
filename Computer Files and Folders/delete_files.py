from pathlib import Path as p

root_dir = p("files/November")

for path in root_dir.glob("*"):
    with open(path, "wb") as file:
        file.write(b"")
    path.unlink()
