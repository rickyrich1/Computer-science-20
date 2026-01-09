modes = {
    "Ionian": 1,
    "Dorian": 2,
    "Phrygian": 3,
    "Lydian": 4,
    "Mixolydian": 5,
    "Aeolian": 6
}
#w1 = list(zip(str,modes))
#w1 = zip(modes)
#w2 = dict.modes
print(modes)
w1 = tuple(modes)
print(w1)
w3 = list(modes.keys())
print(w3)
w2 = list(modes.values())
print(w2)
w4 = modes.update({"Locrian": 7})
print(modes)

