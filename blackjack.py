"""Using sys to exit if the player does not want to play."""
import sys

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

start()
