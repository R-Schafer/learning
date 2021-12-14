# printing new list with even numbers only
a_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new_list = []
for num in a_list:
    if num % 2 == 0:
        new_list.append(num)

print(new_list)


# printing a new list with even positions only
a_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new_list = []
for num in range(0, len(a_list)):
    if num % 2 == 0:
        new_list.append(a_list[num])
print(new_list)