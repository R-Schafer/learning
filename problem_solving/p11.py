# data plan
# https://dmoj.ca/problem/coci16c1p1

monthly_data = int(input("How many megabytes do you get per month:\n"))
how_long = int(input("How long have you had the plan:\n"))
used_data = int(input("How many megabytes did you use the first month:\n"))

i = 1
if used_data < monthly_data:
    rollover = 10 - used_data
else:
    rollover = 0
    
while i < how_long:

    used_data_2 = int(input("How much data did you use the following month:\n"))
    monthly_total = monthly_data + rollover
    if used_data_2 < monthly_total:
        rollover = monthly_total - used_data_2
        new_monthly_data = monthly_data + rollover
    elif monthly_total == monthly_data:
        new_monthly_data = monthly_total 
        
    i += 1
print(f"You have {new_monthly_data} megabytes to use next month.")

# shorter way

# monthly_data = int(input("How much data do you get per month:\n"))
# number_of_months = int(input("How long have you had your plan:\n"))

# total_data = monthly_data * (number_of_months + 1)

# for i in range(number_of_months):
#     used = int(input("How much data did you use:\n"))
#     total_data = total_data - used

# print(f"You have {total_data} megabytes available to use next month.")
    
