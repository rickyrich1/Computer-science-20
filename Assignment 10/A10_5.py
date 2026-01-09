def alphabetize(words):
    return sorted(words)

count = int(input("How many words would you like to enter? "))

word_list = []

for i in range(count):
    word = input("Enter a word: ")
    word_list.append(word)

sorted_words = alphabetize(word_list)

for w in sorted_words:
    print(w, end=" ")
