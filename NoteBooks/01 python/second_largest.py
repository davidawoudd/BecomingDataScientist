numbers = [1,3,1,5,10,4]

largest = numbers[0]

snd_largest = numbers[0]

for current in numbers:
    if current > largest:
        snd_largest = largest
        largest = current
    elif current > snd_largest:
        snd_largest = current

print (snd_largest)