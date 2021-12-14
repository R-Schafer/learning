# coin flips

# flipping coin and putting in list
import random
def coins():
    flips = []
    i = 0
    while i < 100:
        if random.randint(0, 1) == 0:
            flips.append("T")
        else:
            flips.append("H")
        i+= 1
    return flips

# looking for a sequence of 6
def sequence(flips):
    i = 0
    j = 1
    while i < len(flips) and j < len(flips):
        if flips[j] == flips[i]:
            j += 1
            if j - i == 6:
                return True
        else:
            i = j
            j = i + 1
    return False

def main():
    counter = 0
    for i in range(10000):
        if sequence(coins()) == True:
            counter += 1

    print(f"The percentage of receiving a streak of 6 is: {counter / 10000 * 100}%")

main()

