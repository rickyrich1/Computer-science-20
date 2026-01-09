D = {
    "H": 1,
    "He": 2,
    "Li": 4
}
D1 = D["H"]
print(D1)
D2 = D["He"]
print(D2)
D4 = D.update({"Li": 3})
print(D)
D5 = D.update({"Be" : 4, "B" : 5})
print(D)
D6 = D.clear()
print(D)
