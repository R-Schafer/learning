# Given two strings, s1 and s2, create a third-string made of the first char of s1 
# then the last char of s2, Next, the second char of s1 and 
# second last char of s2, and so on. Any leftover chars go at the end of the result.

# Given:

# s1 = "Abc"
# s2 = "Xyz"
# Expected Output: AzbycX

s1 = "Abc"
s2 = "Xyz"
new_word = ""

i = 0
j = len(s2)-1

while i < len(s1) or j >= 0:
    if i >= len(s1):
        new_word = new_word + s2[j]
    elif j < 0:
        new_word = new_word + s1[i]
    else:
        new_word = new_word + s1[i] + s2[j]
        
    i = i + 1
    j = j - 1

print(new_word)