dic1 = {
    "david":1,
    "shehata":2
}
dic2 = {
    "kerolos":1,
    "shehata":2
}

for key, value in dic1.items():
    dic2[key] = value

print (dic2)