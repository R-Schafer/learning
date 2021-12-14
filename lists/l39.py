# creating a list from 1-100 that includes the divisors of the input number

number = int(input("Pick a number less than 20:\n"))
divisors = []
for x in range (number, 101):
    if x % number == 0:
        divisors.append(x)

print(divisors)