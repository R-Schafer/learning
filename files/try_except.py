print("Enter 2 numbers and i will divide them")
try:
    first_num = input("Enter your first number:\n")
    second_num = input("Enter your second number:\n")
    answer = int(first_num) / int(second_num)

except ValueError:
    print("You must enter digits.")
except ZeroDivisionError:
    print("You can't divide by 0!")
else:
    print(f"The Answer is: {answer}")


# trying to open a file that doesn't exist - the traceback error is FileNotFoundError
# filename = 'alice.txt'
# with open(filename, encoding='utf-8') as f:
#     contents = f.read()

# so a better way to write the program above is:
# filename = 'alice.txt'
# try:
#     with open(filename, encoding='utf-8') as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f"Sorry, the file {filename} does not exist.")