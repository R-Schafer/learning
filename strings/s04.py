# Arrange string characters such that lowercase letters should come first
# Given an input string with the combination of the lower and upper case arrange 
# characters in such a way that all lowercase letters should come first.

# str1 = PyNaTive
# Expected Output: yaivePNT

str1 = "PyNaTive"
lower = ""
upper = ""
new_word = ""

for letter in str1:
    if letter.islower():
        lower = lower + letter

for letter in str1:
    if letter.isupper():
        upper = upper + letter

new_word = lower + upper
print(new_word)