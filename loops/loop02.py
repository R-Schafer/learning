# 1
# 12
# 123
# 1234
# 12345


for i in range(1, 6):
    row = ""
    for x in range(1, i + 1):
        row = row + str(x)
    print(row)