# Write a code to extract each digit from an integer, in the reverse order
# If the given int is 7536, the output should be “6 3 5 7“, with a space separating the digits.

# just printing

number = 7536
new_number = str(number)
reverse_number = ""

for i in range(len(new_number) -1, -1, -1):
    reverse_number = reverse_number + new_number[i] + " "
print(reverse_number)

# using function

def reverse_number(number):
    new_number = str(number)
    reverse_number = ""

    for i in range(len(new_number) -1, -1, -1):
        reverse_number = reverse_number + new_number[i] + " "
    return reverse_number

print(reverse_number(7536))