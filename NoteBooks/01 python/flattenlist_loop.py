mylist = [
    [1,2],
    [3,4],
    [5,6]
]

result = []

for sublist in mylist:
    for num in sublist:
        result.append(num)

print (result)