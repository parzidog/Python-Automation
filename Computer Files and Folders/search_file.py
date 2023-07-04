from pathlib import Path

root_dir = Path(".")  # Can be changed to any folder that needs to be searched
search_term = input("Enter your search parameter: ")

for path in root_dir.rglob("*"):
    if search_term in path.stem:
        print(path.absolute())
