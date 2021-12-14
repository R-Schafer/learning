# Reverse a given string

str1 = "PYnative"
new_str = ""
for i in range(len(str1)-1, -1, -1):
    new_str = new_str + str1[i]
print(new_str)

# another way to reverse a string:
str1 = "PYnative"
str1 = str1[::-1]
print(str1) 