# https://dmoj.ca/problem/ccc02j2
# AmeriCanadian
# If the word appears to use American spelling, the program should echo the Canadian spelling for the same word. 
# If the word does not appear to use American spelling, it should be output without change. 

# word = input("Please type an American word:\n")
# word_convert = ""
# if len(word) <= 4:
#     word_convert = word
# elif len(word) > 4:
#     for i in range(0, len(word) -1):
#         if word[i] == "o" and word[i + 1] == "r":
#             word_convert = word_convert + "ou"
#         else:        
#             word_convert = word_convert + word[i]

# print(f"That word is spelled {word_convert} in Canada.")

# using a regex
import re
word = input("Please type an American word:\n")
pattern = re.compile("or")
word_convert = pattern.sub("our", word)

print(f"That word is spelled {word_convert} in Canada.")