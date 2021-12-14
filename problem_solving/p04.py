# The Challenge - In this problem, we’ll assume that phone numbers are four digits. 
# A phone number belongs to a telemarketer if its four digits satisfy all three of the following properties:
# The first digit is 8 or 9.
# The fourth digit is 8 or 9.
# The second and third digits are the same.
# For example, a phone number whose four digits are 8119 belongs to a telemarketer.
# Determine whether a phone number belongs to a telemarketer, and indicate whether we 
# should answer the phone or ignore it.

# Input
# There are four lines of input. These lines give the first, second, third, and fourth 
# digits of the phone number, respectively. Each digit is an integer between 0 and 9.

digit_1 = int(input("First digit:\n"))
digit_2  = int(input("Second digit:\n"))
digit_3 = int(input("Third digit:\n"))
digit_4 = int(input("Fourth digit:\n"))

if digit_1 == 8 or digit_1 == 9:
    print("Do not answer")
elif digit_4 == 8 or digit_4 == 9:
    print("Do not answer")
elif digit_2 == digit_3:
    print("Do not answer")
else:
    print("Answer")