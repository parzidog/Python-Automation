file = open("assets/myfile.txt", "w")

file.write("First Text\n")
file.write("Second Text\n")

file.close()

######## OR ########

with open("assets/myfile.txt", "w") as file:
    file.write("First Text\n")
    file.write("Second Text\n")
