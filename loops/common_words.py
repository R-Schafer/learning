word_lst = []
word_counter = {}

i = 0
while i < 10:
    words = input("Enter a word: (feel free to repeat the same word)\n")
    word_lst.append(words)
    i += 1

for word in range(0, len(word_lst)):
    if word_lst[word] not in word_counter:
        word_counter[(word_lst[word])] = 1
    else:
        word_counter[(word_lst[word])] += 1

for i in word_counter.keys():
    print(f"You used {i} {word_counter[i]} times.")
