import sys

list1 = []
done_lst = []

def print_list():
    for x in range(0, len(list1)):
        print(str((x + 1)) + " " + list1[x])

def save_file():
    filename = 'trello.txt'
    encoded = encode(list1)
    with open(filename, 'w') as file:
        file.write(encoded)

# Take list, return string
def encode(lst):
    contents = ""
    for i in range(0, len(lst)):
        contents += lst[i]
        if i < len(lst) - 1:
            contents += ","
    return contents

def load_file():
    global list1
    filename = 'trello.txt'
    with open(filename) as file:
        contents = file.read()
    
    decoded = decode(contents)
    for value in decoded:
        list1.append(value)

# Take string, return list
def decode(s):
    values = []
    value = ""
    for i in range(0, len(s)):
        if s[i] != ',':
            value += s[i]
        else:
            values.append(value)
            value = ""
    
    if value != "":
        values.append(value)
    return values

def main():
    print("Welcome to Trello")
    load_file()

    while True:
        user_input = input("Type 'a' to add an item, 's' to show your running list, 'r' to remove an item, 'c' to mark as completed, 'save' to save your list, or 'q' to quit.\n")

        if user_input == 'a':
            items = input("Enter item:\n")
            list1.append(items.title())
            print("Item has been added to list.")

        elif user_input == 's':
            print_list()

        elif user_input == 'r':
            print_list()
            list_item = int(input("Which number do you want to remove?\n"))
            if list_item - 1 not in range(0, len(list1)):
                print("Item not in list")
            else:
                remove_item = list1[list_item - 1]
                list1.remove(remove_item)
                print(f"{remove_item} has been removed.")
                
        elif user_input == 'c':
            print_list()
            list_item = int(input("Which number do you want to mark as completed?\n"))
            if list_item - 1 not in range(0, len(list1)):
                print("Item not in list")
            else:
                completed_item = list1[list_item - 1]
                list1.remove(completed_item)
                done_lst.append(completed_item)
                print(f"{completed_item.title()} has been marked as completed.")

        elif user_input == 'q':
            print("Goodbye!")
            sys.exit()

        elif user_input == 'save':
            save_file()

        else:
            print("Invalid entry.")

main()
