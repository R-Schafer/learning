# Reverse a given number and return true if it is the same as the original number

# just printing
number = input("enter a number: \n")

reverse = ""
for i in range(len(number)-1, -1, -1):
    reverse = reverse + number[i]
    
if reverse == number:
    print(f"{number} is the same front and back.")
else:
    print(f"{number} reversed is {reverse}.")

# testing a function
def reversing_number(number):
    reverse = ""
    for i in range(len(number)-1, -1, -1):
        reverse = reverse + number[i]
    
    if reverse == number:
        return True
    else:
        return reverse

print(reversing_number(number))