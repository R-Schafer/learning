# function to determine if the number is prime

def get_number():
    return int(input("Pick a number:\n"))

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def main():
    number = get_number()
    if is_prime(number):
        print("That is a prime number")
    else:
        print("That is not a prime number")

main()