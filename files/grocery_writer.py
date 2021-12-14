import json

grocery_list = "Milk\nBread\Soda"
filename = 'grocery.json'
with open (filename, 'w') as f:
    json.dump(grocery_list, f)