# creating a new txt file

# this makes your words run together
# filename = 'programming.txt'
# with open(filename, 'w') as file_object:
#     file_object.write("Programming is hard")
#     file_object.write("I love creating new games")

# # you should use \newlines
# filename = 'programming.txt'
# with open(filename, 'w') as file_object:
#     file_object.write("Programming is hard\n")
#     file_object.write("I love creating new games\n")


# appending to a file
# filename = 'programming.txt'
# with open(filename, 'a') as file_object:
#     file_object.write("I also love when something clicks\n")
#     file_object.write("This is a test\n")


# # write a program that prompts the user for their name
# filename = 'guest_book.txt'
# with open(filename, 'a') as file_object:
#     name = input("Enter name:\n")
#     file_object.write(f"{name}\n")

# # looping for names
# filename = 'guest_book.txt'
# with open(filename, 'a') as file_object:
#     while True:
#         name = input("Enter name:\n")
#         print(f"Hi {name}, glad you could make it.") 
#         file_object.write(f"{name}\n")


# # creating files for "try it yourself"
# filename = 'cats.txt'
# with open(filename, 'w') as file_object:
#     file_object.write("Whiskers\nMeow Meow\nMr.Kitty\n")

# filename = 'dogs.txt'
# with open(filename, 'w') as file_object:
#     file_object.write("Mochi\nKolache\nJelly Bean")

filename = 'user2.json'
with open(filename, 'w') as file:
    file.write("[]")