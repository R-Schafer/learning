# Concatenate two lists index-wise

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# Output: ['My', 'name', 'is', 'Kelly']

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
newList = []

x = 0
for x in range(len(list1)):
    newList.append(list1[x] + list2[x])  
    x = x + 1
    
print(newList)