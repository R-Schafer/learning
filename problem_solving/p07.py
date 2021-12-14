# Happy or Sad
# https://dmoj.ca/problem/ccc15j2

# We often include emoticons in our text messages to indicate how we are feeling. 
# The three consecutive characters :-) indicate a happy face and the three consecutive characters :-( 
# indicate a sad face. Write a program to determine the overall mood of a message.

# If the input line does not contain any happy or sad emoticons, output none.
# Otherwise, if the input line contains an equal number of happy and sad emoticons, output unsure.
# Otherwise, if the input line contains more happy than sad emoticons, output happy.
# Otherwise, if the input line contains more sad than happy emoticons, output sad.

happy = ":-)"
sad = ":-("

feelings = input("How are you feeling today?\n")
happy_counter = 0
sad_counter = 0

for i in feelings:
    if happy in feelings:
        happy_counter += 1

    if sad in feelings:
        sad_counter += 1


if happy_counter > sad_counter:
    print("happy")
elif sad_counter > happy_counter:
    print("sad")
elif sad_counter == happy_counter:
    print("unsure")
else:
    print("none")
