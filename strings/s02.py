# Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1
# s1 = "Ault"
# s2 = "Kelly"
# Expected Output: AuKellylt

s1 = "Aultt"
s2 = "Kelly"
new_word = ""
for i in range(0, len(s1) + 1):
    if i < len(s1) // 2:
        new_word = new_word + s1[i]
    
    if i == len(s1) // 2:
        new_word = new_word + s2
        
    if i > len(s1) // 2:
        new_word = new_word + s1[i -1]
        
print(new_word)


