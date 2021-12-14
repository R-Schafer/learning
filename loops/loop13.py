# Write a loop to find the factorial of any number

number = input("Enter a number: \n")
total = 1

for i in range(1, int(number) + 1):
    total = total * i

print(f"The factoral of {number} is {total}.")