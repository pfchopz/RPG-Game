#!/usr/bin/env python3
import fight
import character

from random import randint
from os import system


# Create Global Dicts of player and enemy stats
player = character.Player("Player", 20, 10, 5, 5, 5, 5, 5)
enemy = character.Enemy("Enemy", 10, 6, 3, 2, 3, 2, 2)
actionList = ("Fight", "Magic", "Defend", "Run")


def main():
    # Title Screen
    print("\n\n\n\nMONSTER FIGHT: DON'T LOSE EDITION\n\n\n")
    input("\nPress Enter to continue...")

    fightStart()


def fightStart():
    # Fight loop
    while True:
        system('cls||clear')   # Clear Screen

        #Take players turn
        takeTurn(player, enemy)

        #Take enemy turn if still alive
        if enemy.hp > 0:
            takeTurn(enemy, player)

        #Check if death has happened and break loop
        if player.hp <= 0:
            print(f'\n{player.name} dies.\n')
            break
        elif enemy.hp <= 0:
            print(f'\n{enemy.name} dies.\n')
            break
        else:
            input("\nPress Enter to continue...")


def takeTurn(attacker, defender):
    # Perform one attack progression
    if attacker.isHuman:
        option = showOptions(actionList)
    else:
        option = 1

    # Take action dependent on selection
    if option == 1:   # Action for Fight
        defender.hp -= fight.fightChoice(attacker, defender)
    if option == 2:   # Action for Magic
        pass
    if option == 3:   # Action for Defend
        pass
    if option == 4:   # Action for Run
        pass


def showOptions(menu):
    # Ask user to select an option from menu
    while True:
        # Keep health totals on top
        print(f'\n{player.name} has {player.hp} HP and {player.mp} MP remaining.')
        print(f'{enemy.name} has {enemy.hp} HP and {enemy.mp} MP remaining.\n')

        # Print all options
        print("Pick an option below.")
        optionNum = 1
        for option in menu:
            print(f'{optionNum} {option}')
            optionNum += 1
        print(f'{optionNum} Quit')

        # Get valid user input
        userInput = input("Select Option: ")
        if userInput.isnumeric():
            userInput = int(userInput)
            if userInput == optionNum:
                system('cls||clear')  # Clear Screen
                print("\nQuitting Game.")
                exit()
            elif userInput > 0 and userInput <= len(menu):
                print()
                break
            system('cls||clear')  # Clear Screen
        else:
            system('cls||clear')  # Clear Screen

    return userInput


if __name__ == '__main__':
    main()