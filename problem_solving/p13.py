# French or English
# https://dmoj.ca/problem/ccc11s1
# if the given text has more t and T characters than s and S characters, we will say that it is English.
# if the text has more s and S characters than t and T characters, we will say that it is French.
# if the number of t and T characters is the same as the number of s and S characters, we will say that it is French.

sentence = input("Please enter a sentence:\n")
t_counter = 0
s_counter = 0

for i in sentence:
    if i == "t" or i == "T":
        t_counter += 1
    elif i == "s" or i == "S":
        s_counter += 1

if t_counter > s_counter:
    print("English")
elif t_counter == s_counter:
    print("French")
else:
    print("French")


