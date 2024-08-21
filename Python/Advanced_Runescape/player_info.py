'''
Responsible for Player Information.
'''
class PlayerInfo:
    '''
    Creates Player class.
    '''
    def __init__(self) -> None:
        self.name: str = 'Adventurer'
        self.examine: str = 'Beginner'
        self.membership: bool = False

if __name__ == '__main__':
    print('Please run rs3.py instead.')
