"""Using sys to exit if the player does not want to play."""
import sys
import random as rnd

MONEY = 100000


def start():
    """Starts up and asks if the player wants to play."""
    enter = input("Do you want play blackjack?? Y/N\n")
    if enter == "Y":
        game()
    elif enter == "y":
        game()
    elif enter == "N":
        print("Welp, guess I'm terminating the script.")
        sys.exit()
    elif enter == "n":
        print("Welp, guess I'm terminating the script.")
        sys.exit()
    else:
        print("That's not an answer. Only type 'Y' or 'N'.")
        start()

def game():
    """The actual game"""
    playing = True
    while playing is True:
        player_card_count1 = rnd.randint(1, 13)
        player_card_count2 = rnd.randint(1, 13)
        currentcount = player_card_count1 + player_card_count2
        if currentcount > 21:
            print("You already busted. Hope you did not bet too much!")

start()
