# Find the last position of a substring “Emma” in a given string

# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# Output: Last occurrence of Emma starts at index 43

str1 = "Emma is a data scientist who knows Python. Emma works at google."
word = "Emma"
x = len(str1) - 1
y = len(word) - 1

while x >= 0:
    if str1[x] == word[y]:
        y = y - 1
        if y <= -1:
            print(x)
            break
    else:
        y = len(word) - 1
    x = x - 1

# a shortcut for this is:
index = str1.rfind("Emma")
print(index)
