# Fibonacci

def sequence():
    number = int(input("How many sequences do you want:\n"))
    return calculating_sequence(number)

def calculating_sequence(number):
    if number == 0:
        return [0]
    elif number == 1:
        return [0, 1]
    else:
        sequence_order = [0, 1]
        while len(sequence_order) < number:
            sequence_order.append(sequence_order[-1] + sequence_order[-2])
        return sequence_order

print(sequence())

