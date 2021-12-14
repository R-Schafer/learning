# Special Day
# https://dmoj.ca/problem/ccc15j1
# Write a program that asks the user for a numerical month and numerical day of the month a
# nd then determines whether that date occurs before, after, or on February 18.
# If the date occurs before February 18, output the word Before.
# If the date occurs after February 18, output the word After.
# If the date is February 18, output the word Special.

special = "February 18"
month = int(input("Enter a month (1-12):\n"))
day = int(input("Enter a day (1-31):\n"))

if month == 1:
    print("That is before the special day.")
elif month == 2:
    if day < 18:
        print("That is before the special day.")
    elif day > 18:
        print("That is after the special day.")
    else:
        print("That's the special day!")
else:
    print("That is after the special day.")
