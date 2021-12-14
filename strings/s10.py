# Given an input string, count occurrences of all characters within a string
# str1 = "Apple"
# Outcome: {'A': 1, 'p': 2, 'l': 1, 'e': 1}

str1 = "apple"
counter = {}

for letter in str1:
    if letter in counter:
        counter[letter] = counter[letter] + 1
    else:
        counter[letter] = 1

print(counter)
