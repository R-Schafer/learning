# Find words with both alphabets and numbers

# str1 = "Emma25 is Data scientist50 and AI Expert"
# Output:
# Emma25
# scientist50

def has_number(word):
    for char in word:
        if char.isnumeric():
            return True
    return False

str1 = "Emma25 is Data scientist50 and AI Expert"
words = []
add_word = ""

# split sentence into words
for x in str1:

    if not x.isspace():
        add_word = add_word + x

    else:
        words.append(add_word)
        add_word = ""

words.append(add_word)

# print words that have numbers
for new_word in words:
    if has_number(new_word):
      print(new_word)


