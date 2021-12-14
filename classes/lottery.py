from random import randint

my_numbers = [23, 7, 42, 88, 76]
counter = 0

checking_number = []

i = 0
while i < len(my_numbers):
    pick_num = randint(1, 90)
    if pick_num in my_numbers and pick_num not in checking_number:
        checking_number.append(pick_num)
        i += 1
    else:
        counter += 1
        checking_number = []
        i = 0
    
print(f"It took {counter} times to guess my numbers correctly.")
    


