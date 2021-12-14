def word_letters(word):
    for i in range(0, len(word), 2):
        letter = word[i]
        print(letter)


word_letters("pynative")
word_letters("kitchenettes")
