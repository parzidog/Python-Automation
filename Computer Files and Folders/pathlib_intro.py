from pathlib import Path

# Generic way to grab text from files

p1 = "files/abc.txt"

with open(p1, "r") as file:
    print(file.read())

# With Pathlib

p1 = Path("files/ghi.txt")

if not p1.exists():
    with open(p1, "w") as file:
        file.write("Content 3")

with open(p1, "r") as file:
    print(file.read())

# Iterate over files

p2 = Path("files")

for item in p2.iterdir():
    print(item)
