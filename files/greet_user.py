import json

# filename = 'username.json'
# with open(filename) as f:
#     username = json.load(f)
#     print(f"Welcome back {username}!")

# another example with try and except
filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What's your name?\n")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")        
