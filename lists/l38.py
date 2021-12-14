# get the difference between the two lists.

def difference(values, items):
    sum = 0
    sum2 = 0
    for i in values:
        sum = sum + i
    for j in items:
        sum2 = sum2 + j

    if sum2 - sum > 0:
        return sum2 - sum
    elif sum - sum2 > 0:
        return sum - sum2
    else:
        return 0

def main():
    print(difference([5, 5, 8], [5, 5, 5]))

main()