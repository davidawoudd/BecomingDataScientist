mylist = [1,1,2,3,4,4,5]

duplicates = {}
mylist2 = []
for num in mylist:
    if num in duplicates:
        duplicates[num]+=1
    else:
        duplicates[num]=1

for key, value in duplicates.items():
    if value > 1:
        mylist2.append(key)

print (mylist2)