# adding a number to a list after checking and making sure it wasn't in the list already

a_list = list("123456789")

# getting the user's input
def user_number():
    return input("write a number:\n")

# checking to see if the user's number is already in the lsit
def comparing_numbers(number):
    if number not in a_list:
        a_list.append(number)
        return True
    else:
        return False

def main():
    number = user_number()
    if comparing_numbers(number):
        print(f"{number} has been added to your list.")
    else:
        print(f"{number} is already in your list.")

main()