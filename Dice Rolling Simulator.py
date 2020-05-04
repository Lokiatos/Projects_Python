# 1. Dice Rolling Simulator
# The Goal: Like the title suggests, this project involves writing a program that simulates #rolling dice. When the program runs, it will randomly choose a number between 1 and 6. (Or #whatever other integer you prefer — the number of sides on the die is up to you.) The #program will print what that number is. It should then ask you if you’d like to roll #again. For this project, you’ll need to set the min and max number that your dice can #produce. For the average die, that means a minimum of 1 and a maximum of 6. You’ll also #want a function that randomly grabs a number within that range and prints it.
# Concepts to keep in mind:
# Random
# Integer
# Print
# While Loops

import random


def rolling(side):
    number = random.randint(1, side)
    print(f'\nIn a {side} sides dice, we got randomly the number {number}')
    return


repeat = True
side = 0
while repeat == True or side < 3:
    side = int(input("\nInput here the number of sides of this dice: "))
    if side < 3:
        print('A dice need to have a minimun of 3 sides. Please, try again')
    else:
        rolling(side)
        repeat = (str(input('If do you want to roll again press "y"')))
        if repeat.lower() == 'y':
            repeat = True
        else:
            repeat == False
print('Goodbye ^^')
