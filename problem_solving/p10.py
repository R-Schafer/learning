# occupy parking
# https://dmoj.ca/problem/ccc18j2

spaces = int(input("How many spaces in the garage (1-20):\n"))
day1 = input("First day - Put a 'c' for the spaces with a car and a '-' for empty spaces:\n")
day2 = input("Second day - Put a 'c' for the spaces with a car and a '-' for empty spaces:\n")

occupied = 0
for x in range(0, len(day1)):
    if day1[x] == 'c' and day2[x] == 'c':
        occupied += 1

print(f"{occupied} were occupied both days.")
    
