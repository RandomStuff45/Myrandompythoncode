"""Just blackjack"""

# pylint: disable=redefined-outer-name, global-statement

import sys
import re
import random as rnd
import time

money = 100000

def playagain():
    """Asks to play again if the player already played"""
    play_again = input("Do you want to play again? Y/N\n")
    if play_again == "Y":
        print("Ok, playing again in 3...")
        time.sleep(1)
        print("Ok, playing again in 2...")
        time.sleep(1)
        print("Ok, playing again in 1...")
        time.sleep(1)
        gamepart1()
    elif play_again == "y":
        print("Ok, playing again in 3...")
        time.sleep(1)
        print("Ok, playing again in 2...")
        time.sleep(1)
        print("Ok, playing again in 1...")
        time.sleep(1)
        gamepart1()
    elif play_again == "N":
        print("Welp, guess I'm terminating the script.")
        time.sleep(2)
        sys.exit()
    elif play_again == "n":
        print("Welp, guess I'm terminating the script.")
        time.sleep(2)
        sys.exit()

def start():
    """Starts up and asks if the player wants to play."""
    enter = input("Do you want play blackjack?? Y/N\n")
    if enter == "Y":
        gamepart1()
    elif enter == "y":
        gamepart1()
    elif enter == "N":
        print("Welp, guess I'm terminating the script.")
        time.sleep(2)
        sys.exit()
    elif enter == "n":
        print("Welp, guess I'm terminating the script.")
        time.sleep(2)
        sys.exit()
    else:
        print("That's not an answer. Only type 'Y' or 'N'.")
        start()


def gamepart1():
    """The actual game part 1"""
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
    if player_card_count1 == player_card_count2:
        gamepart2s()
    else:
        gamepart2n()

start()
