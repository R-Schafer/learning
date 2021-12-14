# calculator

import re

while True:
    print("Type 'quit' to quit or type numbers:\n")
    text = input()
    if text == 'quit':
        break
    else:

        calc = re.compile(r'(\d+)(\+|-|/|\*)(\d+)')
        numbers = calc.search(text)

        num1 = int(numbers.group(1))
        op = numbers.group(2)
        num2 = int(numbers.group(3))

        answer = None

        if op == "+":
            answer = num1 + num2
        elif op == "-":
            answer = num1 - num2
        elif op == "/":
            answer = num1 // num2
        elif op == "*":
            answer = num1 * num2

        print(answer)

