# Below are the two lists convert it into the dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
numbers = {}

for i in range(len(keys)):
    numbers[keys[i]] = values[i]

print(numbers)