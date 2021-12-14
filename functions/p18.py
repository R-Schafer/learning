# Given two lists of numbers, create a new list that contain only 
# odd numbers from the first list and even numbers from the second list

# list1 =  [10, 20, 23, 11, 17]
# list 2 = [13, 43, 24, 36, 12]

# just printing
list1 =  [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]

new_list = []

for i in range(0, len(list1)):
    if list1[i] % 2 != 0:
        new_list = new_list + [list1[i]]

for i in range(0, len(list2)):
    if list2[i] % 2 == 0:
        new_list = new_list + [list2[i]]

print(new_list)

# using a function

def new_list(list1, list2):
    new_list = []

    for i in range(0, len(list1)):
        if list1[i] % 2 != 0:
            new_list = new_list + [list1[i]]

    for i in range(0, len(list2)):
        if list2[i] % 2 == 0:
            new_list = new_list + [list2[i]]

    return new_list

print(new_list(list1 =  [10, 20, 23, 11, 17], list2 = [13, 43, 24, 36, 12]))