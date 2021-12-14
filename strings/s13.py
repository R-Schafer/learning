# Split a given string on hyphens into several substrings and display each substring

# str1 = Emma-is-a-data-scientist
# Output:
# Emma
# is
# a
# data
# scientist

str1 = "Emma-is-a-data-scientist"

for word in str1.split("-"):
    print(word)