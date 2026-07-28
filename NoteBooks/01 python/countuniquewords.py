text = "david shehata dawoud shehata"

words = text.split()
unique = set()

for word in words:
    unique.add(word)
print (len(unique))