# Calorie counting
# https://dmoj.ca/problem/ccc06j1

print(
    """ Here are the three burger choices:
        1 – Cheeseburger (461 Calories)
        2 – Fish Burger (431 Calories)
        3 – Veggie Burger (420 Calories)
        4 – no burger"""
)
burger = int(input("Which burger would you like:\n"))

print(
    """Here are the three side order choices:
        1 – Fries (100 Calories)
        2 – Baked Potato (57 Calories)
        3 – Chef Salad (70 Calories)
        4 – no side order"""
)
side = int(input("Which side would you like:\n"))

print(
    """Here are the three drink choices:
        1 – Soft Drink (130 Calories)
        2 – Orange Juice (160 Calories)
        3 – Milk (118 Calories)
        4 – no drink"""
)
drink = int(input("Which drink would you like:\n"))

print(
    """Here are the three dessert choices:
        1 – Apple Pie (167 Calories)
        2 – Sundae (266 Calories)
        3 – Fruit Cup (75 Calories)
        4 – no dessert"""
)
dessert = int(input("Which dessert would you like:\n"))


burger_dict = {1: 461, 2: 431, 3: 420, 4: 0}
side_dict = {1: 100, 2: 57, 3: 70, 4: 0}
drink_dict= {1: 130, 2: 160, 3: 118, 4: 0}
dessert_dict = {1: 167, 2: 266, 3: 75, 4: 0}

total = burger_dict[burger] + side_dict[side] + drink_dict[drink] + dessert_dict[dessert]
print(f"Your choices will be {total} calories.")
