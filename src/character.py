import spells

# Basic class holding stats for any character
class Character:
    def __init__(self, name, hp, mp, attack, defense, magicAttack, magicDefense, speed):
        # Set flexible stats
        self.name = name
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        self.magicAttack = magicAttack
        self.magicDefense = magicDefense
        self.speed = speed

        # Set base stats for reference
        self.hpBase = hp
        self.mpBase = mp
        self.attackBase = attack
        self.defenseBase = defense
        self.magicAttackBase = magicAttack
        self.magicDefenseBase = magicDefense
        self.speedBase = speed

    blocking = False
    isPoisoned = False

    def basicAttack(self, defender):
        """Calculate damage done"""
        if defender.blocking:
            damageDealt = self.attack - round(defender.defense * 1.5)
            if damageDealt <= 0:
                damageDealt = 0
        else:
            damageDealt = self.attack - defender.defense
            if damageDealt <= 1:
                damageDealt = 1

        defender.hp -= damageDealt

        """Print choice to console"""
        print(f'{self.name} uses base attack.')
        print(f'{self.name} hits for {damageDealt} damage.')

    def takePoisonDamage(self):
        self.hp -= 1


# Class for player character
class Player(Character):
    def __init__(self, name, hp, mp, attack, defense, magicAttack, magicDefense, speed):
        super().__init__(name, hp, mp, attack, defense, magicAttack, magicDefense, speed)
    
    isHuman = True

    # List of spell objects
    Spells = [
        spells.MagicBolt(),
        spells.Fireball()
    ]


# Class for enemmy character
class Enemy(Character):
    def __init__(self, name, hp, mp, attack, defense, magicAttack, magicDefense, speed):
        super().__init__(name, hp, mp, attack, defense, magicAttack, magicDefense, speed)
    
    isHuman = False

    # List of spell objects
    Spells = [
        spells.Spit(),
        spells.Harden()
    ]