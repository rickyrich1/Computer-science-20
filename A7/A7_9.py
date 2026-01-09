w1 = int(input("number: "))
w2 = int(input("second number:  "))
w3 = int(input("third number: "))
if w1 == w2 == w3:
    print(3)
elif w1 == w2 or w1==w3 or w2 == w3:
    print(2)
else:
    print(0)
