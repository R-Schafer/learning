# enumerate()
# Instead of using the range(len(someList)) technique with a for loop to obtain 
# the integer index of the items in the list, you can call the enumerate() function instead. 
# On each iteration of the loop, enumerate() will return two values: 
# the index of the item in the list, and the item in the list itself.

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print(f"The item at index {index} is: {item}")