# Write a Python program to sum all the items in a list.

def find_sum(items):
    sum = 0
    for i in items:
        sum = sum + i
    return sum

def main():
    print(find_sum([5, 10, 15, 20]))

main()