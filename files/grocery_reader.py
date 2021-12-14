import json

filename = 'grocery.json'
with open(filename) as f:
    grocery = json.load(f)

print(grocery)