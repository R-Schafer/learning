# Write a Python program to multiply all the items in a list

def multiply(items):
    x = 1
    for i in items:
        x = x * i
    return x

def main():
    print(multiply([5, 2, 3]))

main()