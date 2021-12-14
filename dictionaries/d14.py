# How to copy a dictionary and have the option to edit and manipulate the copy. 

dict1 = {'name': 'Rainey', 'age': 32, 'city': 'Cedar Park'}

dict2 = dict(dict1)

dict2['pets'] = 1

print(dict1)
print(dict2)