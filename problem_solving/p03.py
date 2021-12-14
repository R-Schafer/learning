# The Challenge - 
# In basketball, three plays score points: a three-point shot, a two-point shot, and a one-point free throw.
# You just watched a basketball game between the Apples and Bananas and recorded 
# the number of successful three-point, two-point, and one-point plays for each team. 
# Indicate whether the game was won by the Apples, the game was won by the Bananas, or the game was a tie.

# Input
# The first 3 give the scoring for the Apples, and the last 3 give the scoring for the Bananas.
# 1.The first line gives the number of successful three-point shots for the Apples.
# 2.The second line gives the number of successful two-point shots for the Apples.
# 3.The third line gives the number of successful one-point free throws for the Apples.
# 4.The fourth line gives the number of successful three-point shots for the Bananas.
# 5.The fifth line gives the number of successful two-point shots for the Bananas.
# 6.The sixth line gives the number of successful one-point free throws for the Bananas.
# Each number is an integer between 0 and 100.

Ap_3 = int(input("How many 3 pointers for the Apples:\n"))
Ap_2 = int(input("How many 2 pointers for the Apples:\n"))
Ap_1 = int(input("How many free throws for the Apples:\n"))
Ba_3 = int(input("How many 3 pointers for the Bananas:\n"))
Ba_2 = int(input("How many 2 pointers for the Bananas:\n"))
Ba_1 = int(input("How many free throws for the Bananas:\n"))

apple_sum = Ap_3 * 3 + Ap_2 * 2 + Ap_1
banana_sum = Ba_3 * 3 + Ba_2 * 2 + Ba_1

if apple_sum == banana_sum:
    print(f"The teams tied with a score of {apple_sum}.")
elif apple_sum > banana_sum:
    print(f"The Apples won with a score of {apple_sum}.")
else:
    print(f"The Bananas won with a score of {banana_sum}.")