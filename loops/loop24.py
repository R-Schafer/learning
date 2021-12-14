# Print downward Half-Pyramid Pattern with Star (asterisk)
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

for i in range(1, 6):
    row = ""
    for x in range(i, 6):
        row = row + "*"
    print(row)