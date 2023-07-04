from pathlib import Path
from datetime import datetime

root_dir = Path("files")
file_paths = root_dir.iterdir()

# # Complicated Way of doing it

# for path in file_paths:
#     if path.is_dir():
#         for filepath in path.iterdir():
#             print(filepath)


# # More efficient way

# file_paths = root_dir.glob("**/*")

# for path in file_paths:
#     if path.is_file() and path.parts[-2] != "files":
#         parent_folder = path.parts  # Gives an array of the path
#         folder = path.parts[-2]
#         new_filename = folder + "-" + path.name
#         new_filepath = path.with_name(new_filename)
#         path.rename(new_filepath)

# Add date to file name

path = Path("files/December/abc.txt")
stats = path.stat()
second_created = stats.st_ctime
date_created = datetime.fromtimestamp(second_created)
date_str = date_created.strftime("%Y-%m-%d_%H:%M:%S")

print(stats)
print(date_str)
