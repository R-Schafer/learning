# 1
# 2 2
# 3 3 3

for x in range(1, 4):
    answer = ""
    for i in range(x):
        answer = answer + str(x) + " "
    print(answer)


# 1 1 1
# 2 2 2
# 3 3 3

for x in range(1, 4):
    answer = ""
    for i in range(1, 4):
        answer = answer + str(x) + " "
    print(answer)
