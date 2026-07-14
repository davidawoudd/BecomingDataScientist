students = [
    ("David", 100),
    ("Shenoda", 50),
    ("kerlols",95)
]

result = sorted(students, key=lambda student: student[1],reverse=True)

print (result)