# Print multiplication table form 1 to 10


for y in range(1, 11):
    row = ""
    for x in range(1, 11):
        row = row + str(x * y)
    print(row)