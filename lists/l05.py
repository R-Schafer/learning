# Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# Output:
# 10 400
# 20 300
# 30 200
# 40 100

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
x = 0
while x < len(list1):
    str1 = ""
    for y in range(len(list2) -1, -1, -1):
        str1 = str(list1[x]) + " " + str(list2[y])
        x = x + 1
        print(str1)

# Charlie's version:

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
x = 0
y = len(list2) - 1

while x < len(list1) and y >= 0:
    str1 = str(list1[x]) + " " + str(list2[y])
    print(str1)

    x = x + 1
    y = y - 1