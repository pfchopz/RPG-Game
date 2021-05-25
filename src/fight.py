def fightChoice(attacker, defender):
    """Calculate damage done"""
    if defender.blocking:
        damageDealt = attacker.attack - defender.defense * 1.5
        if damageDealt <= 0:
            damageDealt = 0
    else:
        damageDealt = attacker.attack - defender.defense
        if damageDealt <= 1:
            damageDealt = 1

    defender.hp -= damageDealt

    """Print choice to console"""
    print(f'{attacker.name} uses base attack.')
    print(f'{attacker.name} hits for {damageDealt} damage.')

