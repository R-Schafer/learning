# .setdefault()
# .get()

# .setdeafult = it adds the key & value if they are not already in the dictionary. If they are
# already in the dictionary, .setdefault does nothing. 
dict = {'name': 'Rainey', 'age': 32}
dict.setdefault('sex', 'female')
print(dict)
dict.setdefault('sex', 'male')
print(dict)

# .get allows you to look for a key within the dictionary. 
# If it is not there, you use the fallback value (in the example below the fallback value is 0).
# .get does not alter the dictionary
dict = {'name': 'Rainey', 'age': 32}
dict.get('pets', 0)
print(f"Rainey has {dict.get('pets', 0)} pets.")
print(f"Rainey is {dict.get('age', 0)} years old.")

