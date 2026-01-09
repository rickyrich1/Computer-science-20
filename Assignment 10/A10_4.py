w1 = input("enter: ")
w2 = input("enter: ")
def myfunction():
    w3 = len(w1)
    w4 = len(w2)
    w5 = w3 - w4
    w6 = w4 - w3
    if w5 > 0:
        print(f"{w1} has {w5} more character than {w2}")
    elif w6 > 0:
        print(f"{w2} has {w6} more character than {w1}")
    else:
        print(f"Both names have the same number of characters.")
myfunction()
