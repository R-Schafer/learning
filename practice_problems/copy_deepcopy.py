# copy()
# copy.copy(), can be used to make a duplicate copy of a mutable value like a list or dictionary
# deepcopy()
# If the list you need to copy contains lists, then use the copy.deepcopy() function instead of copy.copy(). 
# The deepcopy() function will copy these inner lists as well.

import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42

print(spam)
print(cheese)


spam = ['A', 'B', 'C', 'D', [42, 43]]
cheese = copy.deepcopy(spam)
cheese[4][0] = 'Cat'

print(spam)
print(cheese)
