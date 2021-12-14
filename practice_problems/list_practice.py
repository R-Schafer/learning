# comma code
# Given = spam = ['apples', 'bananas', 'tofu', 'cats']
# Outcome = 'apples, bananas, tofu, and cats'

str = ""
spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs', 'rabbit']
for i in spam:
    if i == spam[-1]:
        str = str + 'and ' + i
    else:
        str = str + i + ', '
print(str)

# coin flip streaks
# Write a program to find out how often a streak of six heads or a streak of six tails 
# appears randomly. Your program breaks up the experiment into two parts: 
# the first part generates a list of randomly selected 'heads' and 'tails' values, 
# and the second part checks if there is a streak in it. 
# Put all of this code in a loop that repeats the experiment 10,000 times so we can find out 
# what percentage of the coin flips contains a streak of six heads or tails in a row.

import random
# Code that creates a list of 100 'heads' or 'tails' values.
def create_flips(count):
    flips = []
    flip = 0
    while flip <= count:
        if random.randint(0, 1) == 0:
            flips.append('H')
        else:
            flips.append('T')
        flip += 1
    return flips

# Code that checks if there is a streak of 6 heads or tails in a row.

def find_streak(flips, streak):
    counter = 1
    prev_letter = None

    for letter in flips:
        if prev_letter == None:
            prev_letter = letter

        elif letter == prev_letter:
            counter += 1
            if counter == streak:
                return True
        else:
            counter = 1

        prev_letter = letter
    return False

# determining probability of streak within each list
num_streaks = 0
i = 1
while i <= 10000:
    flips = create_flips(100)
    has_streak = find_streak(flips, 6)

    if has_streak:
        num_streaks += 1

    i += 1

chance = (num_streaks / 10000) * 100
print(f'Chance of streak: {chance}%')

# character picture grid
# Given = grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]

# Outcome = ..OO.OO..
#           .OOOOOOO.
#           .OOOOOOO.
#           ..OOOOO..
#           ...OOO...
#           ....O....

grid = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']
    ]
x = 0
while x < len(grid[0]):
    y = 0
    s = ""
    while y < len(grid):
        s += grid[y][x]
        y += 1
    print(s)
    x += 1