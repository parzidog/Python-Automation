with open("assets/file3.csv", "r") as file:
    content = file.read()

with open("assets/file3-new.csv", "w") as file:
    file.write(content[:-1])
