# Count all lower case, upper case, digits, and special symbols from a given string

# str1 = "P@#yn26at^&i5ve"
# Expected Outcome: 
# Total counts of chars, digits,and symbols 
# Chars = 8 
# Digits = 3 
# Symbol = 4

str1 = "P@#yn26at^&i5ve"
upper = 0
lower = 0
digits = 0
characters = 0

for x in str1:
    if x.isupper():
        upper = upper + 1

    elif x.islower():
        lower = lower + 1

    elif x.isnumeric():
        digits = digits + 1

    else:
        characters = characters + 1
print(f"Total counts:\nUpper: {upper}\nLower: {lower}\nDigits: {digits}\nSymbols: {characters} " )
