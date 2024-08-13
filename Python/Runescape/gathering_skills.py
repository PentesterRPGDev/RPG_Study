''' Create gathering skills for the game. '''
class GatheringSkills:
    ''' Create class for gathering skills. '''
    def __init__(self) -> None:
        self.wc_lvl: int = 1

    def get_wc_lvl(self) -> int:
        ''' Getter for wc skill. '''
        return self.wc_lvl

    def set_wc_lvl(self, wc_lvl: int) -> None:
        ''' Setter for wc skill. '''
        self.wc_lvl = wc_lvl

if __name__ == '__main__':
    print('Please run rs3.py instead.')
