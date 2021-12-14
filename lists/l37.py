# Shuffle and print list.

import random

def shuffle_list(values):
    random.shuffle(values)
    return values

def main():
    print(shuffle_list([10, 20, 30, 40, 50, 60]))

main()

 

