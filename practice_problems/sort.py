spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)

# reverse sort
spam.sort(reverse=True)
print(spam)
# another way to reverse
spam.reverse()
print(spam)

# Capital letters come before lowercase letter
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)

# If you dont want the letter casing to matter
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)

