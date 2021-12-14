# Remove special symbols/Punctuation from a given string
# str1 = "/*Jon is @developer & musician"
# Output: "Jon is developer musician"

str1 = "/*Jon is @developer & musician"

# removes all characters
new_str= ""
for char in str1:
    if char.isalpha() or char.isspace():
        new_str = new_str + char

# removes the double spaces
str1 = new_str
new_str = ""

prev_char = ""
for char in str1:
    if not char.isspace() or not prev_char.isspace():
        new_str = new_str + char

    prev_char = char

print(new_str)



