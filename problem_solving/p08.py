# Whose in the middle
# https://dmoj.ca/problem/ccc07j1

# Write a program that reads in three weights and prints out the weight of Mama Bear's bowl. 
# You may assume all weights are positive integers less than 100.
while True:
    number1 = int(input("Enter the first weight:\n"))
    number2 = int(input("Enter the second weight:\n"))
    number3 = int(input("Enter the third weight:\n"))

    if number1 == number2 or number1 == number3 or number2 == number3:
        print("Do not repeat numbers")
    elif number1 < number2 and number1 > number3:
        print(number1)
        break
    elif number1 > number2 and number1 < number3:
        print(number1)
        break
    elif number2 < number1 and number2 > number3:
        print(number2)
        break
    elif number2 > number1 and number2 < number3:
        print(number2)
        break
    elif number3 < number1 and number3 > number2:
        print(number3)
        break
    else:
        print(number3)
        break
