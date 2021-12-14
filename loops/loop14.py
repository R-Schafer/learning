# Reverse a given integer number

number = input("Enter a number: \n")
reversed_num = ""

for i in range(len(number)-1, -1, -1):
    reversed_num = reversed_num + number[i]
print(f"{number} reversed is {reversed_num}.")

