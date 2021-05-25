def fightChoice(attacker, defender):
    """Calculate damage done"""
    damageDealt = attacker.attack - defender.defense
    if damageDealt <= 1:
        damageDealt = 1

    """Print choice to console"""
    print(f'{attacker.name} uses base attack.')
    print(f'{attacker.name} hits for {damageDealt} damage.')

    return damageDealt