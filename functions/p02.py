def number_value(rng):
    previous_number = None

    for value in rng:
        if previous_number == None:
            previous_number = value

        sum = value + previous_number
        print(f"Current number: {value} Previous number: {previous_number} Sum: {sum}")

        previous_number = value


number_value(range(0, 10))
number_value(range(0, 11, 2))
