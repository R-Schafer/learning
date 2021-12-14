# memory

# This creates a list
eggs = ['cat', 'dog'] 
print(id(eggs))

# eggs still refers to the same list as before.
eggs.append('moose')
print(id(eggs)) 

# This creates a new list, which has a new identity/list.
eggs = ['bat', 'rat', 'cow'] 
print(id(eggs))
