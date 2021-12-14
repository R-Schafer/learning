# The Challenge - Count the number of words provided. 
# For example, hello is a word, but so are non-English “words” like bbaabbb.

words = input("Please enter a sentence:\n")
counter = 0
for i in words:
    if i == " ":
        counter += 1
        
if words[-1]!= " ":
        counter += 1
print(counter)