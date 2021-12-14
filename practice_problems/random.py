# Using the random.choice() and random.shuffle() Functions with Lists
# The random module has a couple functions that accept lists for arguments. 
# The random.choice() function will return a randomly selected item from the list.

import random
pets = ['Dog', 'Cat', 'Moose']
print(random.choice(pets))

# The random.shuffle() function will reorder the items in a list. 
# This function modifies the list in place, rather than returning a new list. 

import random
people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
print(people)



