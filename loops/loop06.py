# Given a number count the total number of digits in a number
# for ex. 75869 should be 5

number = input("enter a number: \n")
counter = 0
for i in range(1, len(number) + 1):
    counter = counter + 1
print(counter)