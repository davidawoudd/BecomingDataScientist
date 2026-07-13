txt = input("enter a text ")

reversed_txt = txt[::-1]

if txt == reversed_txt:
    print (txt , "is a palindrome")
else:
    print (txt, "is not a palindrome")