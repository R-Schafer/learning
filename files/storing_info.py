# Remember_me.py is also linked to username.json)

import json

username = input("What's your name?\n")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")