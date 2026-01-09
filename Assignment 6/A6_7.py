w1 = input("enter a word with as many h: ")
w2 = w1.find("h")
w3 = w1.rfind("h")
w4 = w1[:w2 + 1] + w1[w2+1:w3].replace("h","H") + w1[w3:]
print(w4)
