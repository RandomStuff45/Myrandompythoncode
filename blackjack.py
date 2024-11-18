"""Just blackjack"""

# pylint: disable=redefined-outer-name, global-statement

import sys
import re
import random as rnd
import time

money = 100000

def playagain():
    play_again = input("Do you want to play again? Y/N\n")
    if play_again ==

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
    global money
    amount_betting_input = input("How much are you betting?\n")
    amount_betting = int(re.search(r'\d+', amount_betting_input).group())
    playing = True
    while playing is True:
        player_card_count1 = rnd.randint(1, 13)
        player_card_count2 = rnd.randint(1, 13)
        current_count = player_card_count1 + player_card_count2
        if current_count > 21:
            print("You already busted. Hope you did not bet too much!")
            current_money = money - amount_betting
            money = current_money
            playagain()
        else:
            input(f"Your current card value is {current_count}. Press any key to continue.")



start()
