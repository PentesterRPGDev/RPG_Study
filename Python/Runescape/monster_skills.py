'''

Organize monster combat skills separated for better design.

'''
class MonsterSkills:
    ''' Responsible for all combat skills of the Monster class. '''
    def __init__(self, health: int, attack: int, strength: int, defense: int) -> None:
        self.health = health
        self.attack = attack
        self.strength = strength
        self.defense = defense

if __name__ == '__main__':
    print('Please run runescape_simulation.py instead.')
