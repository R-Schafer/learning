# Reverse the following list using for loop
# list1 = [10, 20, 30, 40, 50]
# 50
# 40
# 30
# 20
# 10


list1 = [10, 20, 30, 40, 50]
for i in range(len(list1) - 1, -1, -1):
    print(list1[i])
