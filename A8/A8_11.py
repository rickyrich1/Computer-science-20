w1 = input("").split()
w2 = list(map(int,w1))
w3 = max(w2)
w4 = min(w2)
w5 = w2.index(w3)
w6 = w2.index(w4)
w7 = w3[2],w4[4]= w4[4],w3[2]
#print(w5)
print(w7)
