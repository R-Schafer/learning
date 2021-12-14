# Display the cube of the number up to a given integer

number = input("Enter number: \n")

for i in range(1, int(number) + 1):
    cubed_num = i * i * i
    print(f"Current number is :{i} and the cube is: {cubed_num}.")