# Class for spells
class spell:
    def __init__(self, name, power, cost):
        self.name = name
        self.power = power
        self.cost = cost


# Class for Magic Bolt
class MagicBolt(spell):
    def __init__(self):
        self.name = "Magic Bolt"
        self.power = 1
        self.cost = 2

    def __repr__(self):
        return self.name
    
    def useSpell(self, attacker, defender):
        # Check attacker has enough mp
        if attacker.mp >= self.cost:
            # Calculate damage
            damageDealt = (attacker.magicAttack * self.power) - defender.magicDefense
            if damageDealt <= 1:
                damageDealt = 1
            
            # Print actions
            print(f'{attacker.name} uses {self.name}.')
            print(f'{self.name} hits for {damageDealt} damage.')

            # Apply spell effects
            attacker.mp -= self.cost
            defender.hp -= damageDealt

        else:   # Print failed cast if not enough MP
            print(f'{attacker.name} did not have enough MP to cast {self.name}')
            print('No damage was done')


# Class for Fireball
class Fireball(spell):
    def __init__(self):
        self.name = "Fireball"
        self.power = 2
        self.cost = 5

    def __repr__(self):
        return self.name
    
    def useSpell(self, attacker, defender):
        # Check attacker has enough mp
        if attacker.mp >= self.cost:
            # Calculate damage
            damageDealt = (attacker.magicAttack * self.power) - defender.magicDefense
            if damageDealt <= 1:
                damageDealt = 1
            
            # Print actions
            print(f'{attacker.name} uses {self.name}.')
            print(f'{self.name} hits for {damageDealt} damage.')

            # Apply spell effects
            attacker.mp -= self.cost
            defender.hp -= damageDealt

        else:   # Print failed cast if not enough MP
            print(f'{attacker.name} did not have enough MP to cast {self.name}')
            print('No damage was done')


# Class for Spit
class Spit(spell):
    def __init__(self):
        self.name = "Spit"
        self.power = 1
        self.cost = 2

    def __repr__(self):
        return self.name
    
    def useSpell(self, attacker, defender):
        # Check attacker has enough mp
        if attacker.mp >= self.cost:
            # Calculate damage
            damageDealt = (attacker.magicAttack * self.power) - defender.magicDefense
            if damageDealt <= 1:
                damageDealt = 1
            
            # Print actions
            print(f'{attacker.name} uses {self.name}.')
            print(f'{self.name} hits for {damageDealt} damage.')

            # Apply spell effects
            attacker.mp -= self.cost
            defender.hp -= damageDealt

        else:   # Print failed cast if not enough MP
            print(f'{attacker.name} did not have enough MP to cast {self.name}')
            print('No damage was done')


# Class for Harden
class Harden(spell):
    def __init__(self):
        self.name = "Harden"
        self.power = 1
        self.cost = 2

    def __repr__(self):
        return self.name
    
    def useSpell(self, attacker, defender):
        # Check attacker has enough mp
        if attacker.mp >= self.cost:            
            # Print actions
            print(f'{attacker.name} uses {self.name}.')
            print(f'{self.name} defense increased by {self.power}.')

            # Apply spell effects
            attacker.mp -= self.cost
            defender.defense += self.power

        else:   # Print failed cast if not enough MP
            print(f'{attacker.name} did not have enough MP to cast {self.name}')
            print('No damage was done')