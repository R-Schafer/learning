# Given a range of the first 10 numbers, 
# Iterate from the start number to the end number, 
# and In each iteration print the sum of the current number and previous number

# just printing
sum = 0
for i in range(1, 10):
    current = i
    previous = i -1
    sum = current + previous

    print(f"Current number: {current}, Previous number: {previous}, Sum: {sum}. ")

# using a function
def numbers(RNG):
    for i in RNG:
        current = i
        previous = i -1
        sum = current + previous

        print(f"Current number: {current}, Previous number: {previous}, Sum: {sum}. ")


numbers(range(1, 10))
numbers(range(0, 11, 2))
