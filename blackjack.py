"""Just blackjack"""

# pylint: disable=redefined-outer-name, global-statement

import sys
import re
import random as rnd
import time

money = 100000
current_count = 0

def gamepart2n():
    global current_count
    hitorstand = input("Enter 1 to hit or 2 to stand.")
    if hitorstand == "1":
        temp_current_count = current_count
        current_count = rnd.randint(1, 13) + temp_current_count
        hitorstand2 = input(f"Your current card count is {current_count}. Press 1 to continue or 2 to stand")
        if hitorstand2 == ""

def gamepart2s():
    print("Enter 1 to hit, 2 to stand, and 3 to split")

def playagain():
    """Asks to play again if the player already played"""
    global money
    play_again = input(f"Do you want to play again? YOur current money amount is ${money} Y/N\n")
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
    enter = input("Do you want to play blackjack? Y/N\n")
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
    global current_count
    global money
    amount_betting_input = input(f"How much are you betting? YOu have ${money}.\n")
    amount_betting = int(re.search(r'\d+', amount_betting_input).group())
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
