# tuples can't be modified
# below will cause an error since 88 can't be changed to 87
# name = ('Rainey', 'hi', 88)
# name[2] = 87
# print(name[2])

# If only 1 item in the tuple add a ',' to the end otherwise Python will think it's a string
name = ("Rainey",)
print(name[0])

# taking a list and converting it to a tuple - you have to use the tuple() function
tuple(['cat', 'dog'])
# assigning the tuple to a variable
items = tuple(['cat', 'dog'])
print(items)

# putting a tuple into a list and being able to modify that list - must use list() function

list(('cat', 'dog'))
items = list(('cat', 'dog'))
items[0] = 'cats'
print(items)

