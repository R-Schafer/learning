# Replace each punctuation with # in the following string

# str1 = '/*Jon is @developer & musician!!'
# Output: ##Jon is #developer # musician##

str1 = '/*Jon is @developer & musician!!'
new_str = ""
for char in str1:
    if char.isalnum() or char.isspace(): 
        new_str = new_str + char
    else:
        new_str = new_str + "#"
print(new_str)