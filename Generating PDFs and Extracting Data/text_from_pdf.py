import fitz

with fitz.open("Resources/students.pdf") as pdf:
    for page in pdf:
        print(20 * "--")
        print(page.get_text())
