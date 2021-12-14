# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

for i in range(5, 0, -1):
    row = ""
    for x in range(i, 0, -1):
        row = row + str(x)
    print(row)


#     *
#    **
#   ***
#  ****
# *****

for i in range(0, 5):
    row = ""
    for x in range(1, 5 - i):
        row = row + " "

    for x in range(0, i + 1):
        row = row + "*"

    print(row)
