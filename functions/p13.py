def mult_table():
    for i in range(1, 11):
        
        row = ""
        for x in range(1, 11):
            row = row + str(i * x) + " "
        print(row)

mult_table()