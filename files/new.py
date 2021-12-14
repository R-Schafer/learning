import json

# save
str = "Rainey"
filename = 'new.json'
with open(filename, 'w') as f:
    json.dump(str, f)


# load
filename = 'new.json'
with open(filename) as f:
    new = json.load(f)
print(new)