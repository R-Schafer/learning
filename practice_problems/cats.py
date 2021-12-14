# Making a list of cat names
catNames = []
while True:
    name = input("Enter your cat's name or enter 'quit' to close the program:\n")

    if name == 'quit':
        break
    else:
        catNames.append(name)

print("Here are the cat names in the list:")
for name in catNames:
    print(f"{name}")
    