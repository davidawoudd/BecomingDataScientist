with open ("DataSets/commands.txt","r") as file:
    longest = ""
    for line in file:
        if len(line) > len(longest):
            longest = line

print (longest)