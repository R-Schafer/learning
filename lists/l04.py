# Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
newList = []

for x in range(0, len(list1)):
    for y in range(0, len(list2)):
        newList.append(list1[x] + list2[y])

print(newList)