# Given a Python list, find value 20 in the list, and if it is present, replace it with 200. 
# Only update the first occurrence of a value

# list1 = [5, 10, 15, 20, 25, 50, 20]
# Output: list1 = [5, 10, 15, 200, 25, 50, 20]

# list1 = [5, 10, 15, 20, 25, 50, 20]

# list1[3] = 200
# print(list1)

# trying to do the loop
list1 = [5, 10, 15, 20, 25, 50, 20]
for i in range(0, len(list1)):
    if list1[i] == 20:
        list1[i] = 200
        break

print(list1)

