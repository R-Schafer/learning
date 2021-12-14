# smarties
# https://dmoj.ca/problem/ecoo15r1p1
import math

colors = {
    "orange": 0,
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "pink": 0,
    "violet": 0,
    "brown": 0,
    "red": 0
}

smarties = "red brown brown violet blue pink blue blue pink brown yellow brown pink violet green yellow red orange orange blue brown pink red red red brown orange orange green red orange violet blue pink yellow pink brown orange green red blue yellow green orange brown orange pink violet brown red"
color = smarties.split(" ")
for i in color:
    if i in colors:
        colors[i] += 1

total_time = 0
for color, amount in colors.items():
    if color == "red":
        time = amount * 16
        total_time += time
    else:
        handfulls = math.ceil(amount / 7)
        time = handfulls * 13
        total_time += time

print(total_time)

