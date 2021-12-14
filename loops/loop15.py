# Use a loop to display elements from a given list that 
# are present at odd index positions
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(0, len(my_list)):
    if i % 2 != 0:
        print(my_list[i])