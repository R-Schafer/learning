import json

filename = 'user2.json'
entry = "Rainey"

with open(filename, 'r') as file:
    username = json.load(file)

username.append(entry)
with open(filename, 'w') as file:
    json.dump(username, file)