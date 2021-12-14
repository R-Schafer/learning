# Removal all the characters other than integers from a string

# str1 = 'I am 25 years and 10 months old'
# Output:2510

str1 = 'I am 25 years and 10 months old'
number = ""
for char in str1:
    if char.isnumeric():
        number = number + char
print(number)