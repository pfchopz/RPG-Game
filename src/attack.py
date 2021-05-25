# Class for attacks
class attack:
    def __init__(self, name, power, cost):
        self.name = name
        self.power = power
        self.cost = cost


# Class for attack spells
class attackSpell(attack):
    def __init__(self, name, power, cost):
        super().__init__(self, name, power, cost)
    
    def useSpell(self, attacker, defender):
        # Check attacker has enough mp
        if attacker.mp >= self.cost:
            # Calculate damage
            damageDealt = (attacker.magicAttack * self.power) - defender.magicDefense
            
            # Print actions
            print(f'{attacker.name} uses {self.name}.')
            print(f'{self.name} hits for {damageDealt} damage.')

            # Apply spell effects
            attacker.mp -= self.cost
            defender.hp -= damageDealt

        else:   # Print failed cast if not enough MP
            print(f'{attacker.name} did not have enough MP to cast {self.name}')
            print('No damage was done')


class defenseSpell(attack):
    def __init__(self, name, power, cost):
        super().__init__(self, name, power, cost)

    def useSpell(self, attacker):
        # Check attacker has enough mp
        if attacker.mp >= self.cost:
            # Print actions
            print(f'{attacker.name} uses {self.name}.')
            print(f'{self.name} gains {self.power} defense.')

            # Apply spell effects
            attacker.mp -= self.cost
            attacker.defense += self.power

        else:   # Print failed cast if not enough MP
            print(f'{attacker.name} did not have enough MP to cast {self.name}')
            print('No damage was done')
