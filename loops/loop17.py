# Find the sum of the series 2 + 22 + 222 + 2222 + .. n terms

number_terms = 5
x = 2
total = ""
sum = 0
for i in range(1, number_terms + 1):
    total = total + str(x)
    sum = sum + int(total)
print(sum)
