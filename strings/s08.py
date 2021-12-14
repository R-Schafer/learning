# Find all occurrences of “USA” in a given string ignoring the case
# str1 = "Welcome to USA. usa awesome, isn't it?"
# Expected Outcome: The USA count is: 2

str1 = "Welcome to USA. usa awesome, isn't it?".lower()
str2 = "USA".lower()
counter = 0
j = 0
for i in range(len(str1)):
    if str1[i] == str2[j]:
        j = j + 1
        if j >= len(str2):
            j = 0
            counter = counter + 1
    else:
        j = 0

print(counter)

