import json

filename = 'numbers.json'
with open(filename) as fo:
    numbers = json.load(fo)

print(numbers)