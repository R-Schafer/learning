# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Case 1:
# base = 2
# exponent = 5
# 2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

# Case 2:
# base = 5
# exponent = 4
# 5 raises to the power of 4 is: 625 
# i.e. (5 *5 * 5 *5 = 625)

def exponent(base, exp):
    new_number = 1
    for i in range(1, exp + 1):
        new_number = new_number * base
    return new_number

print(exponent(5, 4))
print(exponent(2, 5))