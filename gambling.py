"""Using sys to exit if the player does not want to play."""
import sys

MONEY = 100000


def start():
    """Starts up and asks if the player wants to play."""
    enter = input("Do you want to gamble? Y/N\n")
    if enter == "Y":
        choose()
    elif enter == "y":
        choose()
    elif enter == "N":
        print("Welp, guess I'm terminating the script.")
        sys.exit()
    elif enter == "n":
        print("Welp, guess I'm terminating the script.")
        sys.exit()
    else:
        print("That's not an answer. Only type 'Y' or 'N'.")
        start()


def choose():
    """Pick if the player wants blackjack or THE RANDOM MACHINE"""
    choice = input(
        "If you want blackjack type B and if you want THE RANDOM MACHINE type R.\n"
    )
    if choice == "B":
        print("Ok! Activating blackjack now.")
    elif choice == "b":
        print("Ok! Activating blackjack now.")
    elif choice == "R":
        print("Ok! Activating THE RANDOM MACHINE now.")
    elif choice == "r":
        print("Ok! Activating THE RANDOM MACHINE now.")
    else:
        print("That's not an answer. Only type 'B' or 'R'")
        choose()


start()
