# Display Fibonacci series up to 10 terms
# Expected output:
# 0  1  1  2  3  5  8  13  21  34

my_list = [] 
for i in range(10):
    if i <= 1:
        my_list.append(i)
    else:
        my_list.append(my_list[i-1] + my_list[i-2])
print(my_list)