# display all prime numbers within a range of 25-50.

for i in range(25, 50):
    if i > 2:
        for x in range (2, i):
            if i % x == 0:
                break
        else:
            print(i)