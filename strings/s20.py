# making sure input is all lowercase & other .()examples

feeling = input("How are you feeling today?\n")
if feeling.lower() == 'great':
    print("I feel great too")
else:
    print("I hope the rest of your day get better")


spam = 'Hello, world!'
spam.islower()
# False
spam.isupper()
# False
'HELLO'.isupper()
# True
'abc12345'.islower()
# True
'12345'.islower()
# False
'12345'.isupper()
# False
# others
'hello'.isalpha()
# True
'hello123'.isalpha()
# False
'hello123'.isalnum()
# True
'hello'.isalnum()
# True
'123'.isdecimal()
# True
'    '.isspace()
# True
'This Is Title Case'.istitle()
# True
'This Is Title Case 123'.istitle()
#  True
'This Is not Title Case'.istitle()
# False
'This Is NOT Title Case Either'.istitle()
# False