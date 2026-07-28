students = [
    ("David", "CS"),
    ("John", "IT"),
    ("Sara", "CS"),
    ("Ahmed", "AI"),
    ("Mina", "IT")
]
groups = {}

for student, depertment in students:
    if depertment in groups:
        groups[depertment].append(student)
    else:
        groups[depertment] = []
        groups[depertment].append(student)

print(groups)