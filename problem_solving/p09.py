# three cups
# https://dmoj.ca/problem/coci06c5p1

# Three opaque cups: one at the left (location 1), one at the middle (location 2), 
# and one at the right (location 3). There is a ball under the cup at the left. 
# Keep track of the location of the ball.Make three types of swap:
# A Swap the left and middle cups
# B Swap the middle and right cups
# C Swap the left and right cups

user = input("The ball is under the middle cup (position B), left is position A, and right is position C. Enter moves:\n")
moves= user.upper()
print("~~~ moving cups ~~~")
user_guess = input("Where do you think the ball is (A, B, or C):\n")
guess = user_guess.upper()

ball = "B"

for move in moves:
    # swapping left cup with middle cup
    if move == "A" and ball == "B":
        ball = "A"
    elif move == "A" and ball == "A":
        ball = "B"

    # swapping left cup with right cup
    elif move == "B" and ball == "A":
        ball = "C"
    elif move == "B" and ball == "C":
        ball = "A"

    # swapping middle cup and right cup
    elif move == "C" and ball == "B":
        ball = "C"
    elif move == "C" and ball == "C":
        ball = "B"

if ball == guess:
    print("Correct!")
else:
    print(f"Wrong, the ball is at {ball}.")

