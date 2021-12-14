# Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

for x in range(1, 6):
    row = ""
    for i in range(x):
        row = row + str(x)
    print(row)



    