# Reverse a given list in Python
# aList = [100, 200, 300, 400, 500]
# Output: [500, 400, 300, 200, 100]

aList = [100, 200, 300, 400, 500]
newList = []

for i in range(len(aList) - 1, -1, -1):
    newList.append(aList[i])
print(newList)

# a short cut:
aList = [100, 200, 300, 400, 500]
aList = aList[::-1]
print(aList)