# https://learning.oreilly.com/library/view/the-big-book/9781098129026/c04.xhtml

import sys, random
hearts = chr(9829)
diamonds = chr(9830)
spades = chr(9824)
clubs = chr(9827)
backside = 'backside'

def main():
    print(''' Blackjack, by Al Sweigart
    
        Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.''')

    money = 5000
    while True:
        # check if player has money
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing, goodbye!')
            sys.exit()

        # let player enter their bet
        bet = int(input("How much money would you like to bet:\n"))
        
        # deal 2 cards 
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # handle player actions
        print("Bet:", bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            # check if player busted:
            if getHandValue(playerHand) > 21:
                break

            # get players move (hit, stay or double)
            move = getMove(playerHand, money - bet)

            # handle player actions
            if move == 'D':
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print("Bet increased to {}.".format(bet))
                print("Bet:", bet)

            if move in ("H", "D"):
                newCard = deck.pop()
                rank, suit = newCard
                print("You drew a {} of {}.".format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    continue

            if move in ("S", "D"):
                break

        # handle dealers action
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print("Dealer hits...")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break
                input("Press Enter to continue...")
                print("\n\n")

        # Show final hands:
        displayHands(playerHand, dealerHand, True)
        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        # Win, Tie, Lose
        if dealerValue > 21:
            print("Dealer busts! You win ${}!".format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print("You lost!")
            money -= bet
        elif playerValue > dealerValue:
            print("You won ${}!".format(bet))
            money += bet
        elif playerValue == dealerValue:
            print("Tie! The bet is returned to you.")
        
        input("Press enter to continue...")
        print("\n\n")

def getBet(maxBet):
    while True:
        print("How much do you want to bet? (1-{}, or QUIT)".format(maxBet))
        bet = input("> ").upper().strip()
        if bet == 'QUIT':
            print("Thanks for playing, goodbye!")
            sys.exit()
        
        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def getDeck():
    deck = []
    for suit in (hearts, diamonds, spades, clubs):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    # show dealer cards
    if showDealerHand:
        print("DEALER:", getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("DEALER: ???")
        displayCards([backside] + dealerHand[1:])

    # show players cards
    print("PLAYER:", getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    value = 0
    numberOfAces = 0

    # add value to cards
    for card in cards:
        rank = card[0]
        if rank == "A":
            numberOfAces += 1
        elif rank in ("K", "Q", "J"):
            value += 10
        else:
            value += int(rank)

    # add value to aces
    for i in range(numberOfAces):
        if value + 11 <= 21:
            value += 11
        else:
            value += 1

    return value

def displayCards(cards):
    rows = ["", "", "", "", ""]

    for card in cards:
        rows[0] += ' ___  '
        if card == backside:
            rows[1] += " |## | "
            rows[2] += " |###| "
            rows[3] += " |_##| "
        else:
            rank, suit = card
            rows[1] += "|{} | " .format(rank.ljust(2))
            rows[2] += "| {} | " .format(suit)
            rows[3] += "|_{}| " .format(rank.rjust(2, "_"))

    # print each row on screen
    for row in rows:
        print(row)

def getMove(playerHand, money):
    while True:
        moves = ["(H)it", "(S)tay"]
        if len(playerHand) == 2 and money > 0:
            moves.append("(D)ouble down")

        # get players move
        movePrompt = ", " .join(moves) + ":\n"
        move = input(movePrompt).upper()
        if move in ("H", "S"):
            return move
        if move == "D" and "(D)ouble down" in moves:
            return move

main()