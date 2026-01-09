webpages = ['homepage', 'aboutpage', 'sitemap']
w1 = input("Enter three values: ").split()
w2 = list(map(int,w1))
if w2 < 0:
    print("invalid value")
else:
    w3 = dict(zip(webpages , w1))
    print(w3)
