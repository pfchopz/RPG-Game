#!/usr/bin/env python3
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

    fightStart(player, enemy)


def fightStart(attacker, defender):
    # Fight loop
    while True:
        system('cls||clear')   # Clear Screen

        # Pre Fight Phase for both characters
        attackerChoice = preFightPhase(attacker, defender)
        defenderChoice = preFightPhase(defender, attacker)

        # Do the Fight Phase for both characters
        if enemy.hp > 0:
            fightPhase(attacker, defender, attackerChoice)
            fightPhase(defender, attacker, defenderChoice)

        # Reset characters block to false
        attacker.blocking = False
        defender.blocking = False

        # Perform status effects when applicable
        print()
        attacker.takePoisonDamage()
        defender.takePoisonDamage()

        # Check if death has happened and break loop
        if attacker.hp <= 0:
            print(f'\n{attacker.name} dies.\n')
            break
        elif defender.hp <= 0:
            print(f'\n{defender.name} dies.\n')
            break
        else:
            input("\nPress Enter to continue...")


def preFightPhase(attacker, defender):
    # Determine the action choice
    actionChoice = {}

    # Get choice selection
    if attacker.isHuman:
        actionChoice['option'] = showOptions(actionList)
        if actionChoice['option'] == 2:
            actionChoice['spell'] = showOptions(attacker.Spells) - 1     
    else:
        actionChoice['option'] = randint(1,len(actionList) - 1)
        if actionChoice['option'] == 2:
            actionChoice['spell'] = randint(1,len(attacker.Spells)) - 1

    # Carry out defend option if that was character selection
    if actionChoice['option'] == 3:  
        attacker.blocking = True
        print(f'{attacker.name} is defending.')

    # Carry out run option if that was character selection
    if actionChoice['option'] == 4:
        chance = attacker.speed - defender.speed
        print(f'{attacker.name} is attempting to run.')
        if chance > 0:
            if randint(0,1) > 0:
                system('cls||clear')  # Clear Screen
                print(f'\n{attacker.name} successfully escaped the fight.\n')
                exit()
            else:
                print(f'{attacker.name} failed to escape the fight.')
        else:
            print(f'{attacker.name} is too slow to escape.')

    # Return actionChoice dictionary for use during fight phase
    return actionChoice


def fightPhase(attacker, defender, choices):
    # Take action dependent on selection
    if choices['option'] == 1:   # Action for Fight
        attacker.basicAttack(defender)
    if choices['option'] == 2:   # Action for Magic
        attacker.Spells[choices['spell']].useSpell(attacker, defender)
    if choices['option'] == 3:   # Action for Defend
        pass
    if choices['option'] == 4:   # Action for Run
        pass


def showOptions(menu):
    # Ask user to select an option from menu
    while True:
        system('cls||clear')   # Clear Screen

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
                print("\nQuitting Game.\n")
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