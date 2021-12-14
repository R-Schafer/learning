# Program that counts the number of occurrences of each letter in a string.

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

    # Alternative to line 9-10
    # count[character] = count.get(character, 0) + 1
pprint.pprint(count)