# Given two strings, s1, and s2 return a new string made of the first, middle, 
# and last characters each input string

# s1 = "America"
# s2 = "Japan"
# Expected Output: AJrpan

# just printing
s1 = "America"
s2 = "Japan"

new_word = s1[0] + s2[0] + s1[len(s1) // 2] + s2[len(s2) // 2] + s1[-1] + s2[-1]
 
print(new_word)
