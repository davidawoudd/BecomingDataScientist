"""
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in List:
    if num % 2 == 0:
        print(num)

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in List:
    print (num*num)

"""

str = "python is great and python is easy"

words = str.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word] = 1

print (word_count)
 
