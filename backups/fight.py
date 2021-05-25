def fightChoice(attacker, defender):
    """Calculate damage done"""
    damageDealt = attacker['Atk'] - defender['Def']
    if damageDealt <= 1:
        damageDealt = 1

    """Print choice to console"""
    print(f'{attacker["Name"]} uses base attack.')
    print(f'{attacker["Name"]} hits for {damageDealt} damage.')

    return damageDealt

def magicChoice(attacker, defender, spell):
    spellName = list(attacker['Spells'])[spell - 1]
    if attacker['MP'] >= attacker['Spells'][spellName]['MP']:
        return 0
    else:
        return 0