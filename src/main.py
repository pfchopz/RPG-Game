#!/usr/bin/env python3
import fight

from random import randint
from os import system


# Create Global Dicts of player and enemy stats
playerStats = {'Name': "Player", 'HP': 20, 'MP': 10, 'Atk': 5, 'Def': 5, 'Mag': 5, 'MDef': 5, 'Spd': 5, 'Defend': False,
                'Spells': {
                    'Magic Bolt': {'Power': 1, 'MP': 2, 'Type': 'Mag'},
                    'Fireball': {'Power': 2, 'MP': 5, 'Type': 'Mag'}
                }
            }
enemyStats = {'Name': "Enemy", 'HP': 10, 'MP': 6, 'Atk': 3, 'Def': 2, 'Mag': 3, 'MDef': 2, 'Spd': 2, 'Defend': False,
                'Spells': {
                    'Spit': {'Power': 1, 'MP': 2, 'Type': 'Mag'},
                    'Harden': {'Power': 1, 'MP': 2, 'Type': 'Def'}
                 }
            }
player, enemy = playerStats, enemyStats
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
        takeTurn(player, enemy, True)

        #Take enemy turn if still alive
        if enemy['HP'] > 0:
            takeTurn(enemy, player)

        #Check if death has happened and break loop
        if player['HP'] <= 0:
            print(f'{player["Name"]} dies.')
            break
        elif enemy['HP'] <= 0:
            print(f'{enemy["Name"]} dies.')
            break
        else:
            input("\nPress Enter to continue...")


def takeTurn(attacker, defender, humanPlayer = False):
    # Perform one attack progression
    if humanPlayer == False:
        option = 1
        spell = randint(1, len(attacker['Spells']))
    else:
        option = showOptions(actionList)
        if option == 2:
            spell = showOptions(attacker['Spells'])

    # Take action dependent on selection
    if option == 1:   # Action for Fight
        defender['HP'] -= fight.fightChoice(attacker, defender)
    if option == 2:   # Action for Magic
        defender['HP'] -= fight.magicChoice(attacker, defender, spell)
    if option == 3:   # Action for Defend
        pass
    if option == 4:   # Action for Run
        pass


def showOptions(menu):
    # Ask user to select an option from menu
    while True:
        # Keep health totals on top
        print(f'\n{player["Name"]} has {player["HP"]} HP and {player["MP"]} MP remaining.')
        print(f'{enemy["Name"]} has {enemy["HP"]} HP and {enemy["MP"]} MP remaining.\n')

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