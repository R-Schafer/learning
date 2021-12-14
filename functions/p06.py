def divisible_5(numbers):
    for number in numbers:
        if number % 5 == 0:
            print(number)


divisible_5([10, 20, 33, 46, 55])
divisible_5([100])