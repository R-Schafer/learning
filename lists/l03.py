# Given a Python list of numbers. Turn every item of a list into its square
# aList = [1, 2, 3, 4, 5, 6, 7]
# Output: [1, 4, 9, 16, 25, 36, 49]

aList = [1, 2, 3, 4, 5, 6, 7]
newList = []

for i in range(0, len(aList)):
    v = aList[i] * aList[i]
    newList.append(v)
print(newList)