# Given a Python list, remove all occurrence of 20 from the list
# list1 = [5, 20, 15, 20, 25, 50, 20]
# Output: [5, 15, 25, 50]

list1 = [5, 20, 15, 20, 25, 50, 20]

i = 0
while i < len(list1):
    if list1[i] == 20:
        del list1[i]
    else:
        i = i + 1
print(list1)
