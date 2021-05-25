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


# Class for player character
class Player(Character):
    def __init__(self, name, hp, mp, attack, defense, magicAttack, magicDefense, speed):
        super().__init__(name, hp, mp, attack, defense, magicAttack, magicDefense, speed)
    
    isHuman = True

    # Spell objects
    Spells = [
        spells.MagicBolt(),
        spells.Fireball()
    ]


# Class for enemmy character
class Enemy(Character):
    def __init__(self, name, hp, mp, attack, defense, magicAttack, magicDefense, speed):
        super().__init__(name, hp, mp, attack, defense, magicAttack, magicDefense, speed)
    
    isHuman = False