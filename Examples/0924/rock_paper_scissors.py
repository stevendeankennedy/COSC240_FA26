'''
    ROCK PAPER SCISSOR

    Authors:
        Bailey, Dusty, Declan, Cole, Lark
'''
import random

ROCK = 0
PAPER = 1
SCISSORS = 2
words = ["ROCK", "PAPER", "SCISSORS"]

# get input from player
p_in = input("Enter R/P/S/Q >")
while (p_in != "Q"):

    hand = -1

    if p_in == "R" or p_in == "r":
        hand = ROCK
    elif p_in == "P" or p_in == "p":
        hand = PAPER
    elif p_in == "S" or p_in == "s":
        hand = SCISSORS
    else:
        print("Please choose R P or S")

    # get a random option for python

    comp_hand = random.randrange(3)

    print(f'{words[hand]} v {words[comp_hand]}')
    # check to see who won / print results
    if (hand > comp_hand) or (hand == ROCK and comp_hand == SCISSORS):
        print("Player wins!")
    else:
        print("Computer wins!")

    p_in = input("Enter R/P/S/Q >")















