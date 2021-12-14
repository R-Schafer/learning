
# Accept number from user and calculate the sum of all number from 1 to the given number

sum = 0
number = int(input("Enter a number:\n"))
for i in range(1, number + 1):
    sum = sum + i
print(sum)