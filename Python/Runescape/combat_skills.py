''' Combat Skills. '''

class CombatSkills:
    ''' Responsible for all combat skills of the Player class. '''
    def __init__(self) -> None:
        self.hp: int = 99
        self.atk_lvl: int = 1
        self.str_lvl: int = 99
        self.def_lvl: int = 1

    def get_hp(self) -> int:
        ''' Getter for the hp skill. '''
        return self.hp

    def set_hp(self, hp: int) -> None:
        ''' Setter for the hp skill. '''
        self.hp = hp

    def get_atk_lvl(self) -> int:
        ''' Getter for the atk skill. '''
        return self.atk_lvl

    def set_atk_lvl(self, atk_lvl: int) -> None:
        ''' Setter for the atk skill. '''
        self.atk_lvl = atk_lvl

    def get_str_lvl(self) -> int:
        ''' Getter for the str skill. '''
        return self.str_lvl

    def set_str_lvl(self, str_lvl: int) -> None:
        ''' Setter for the str skill. '''
        self.str_lvl = str_lvl

    def get_def_lvl(self) -> int:
        ''' Getter for the def skill. '''
        return self.def_lvl

    def set_def_lvl(self, def_lvl: int) -> None:
        ''' Setter for the def skill. '''
        self.def_lvl = def_lvl

if __name__ == '__main__':
    print('Please run runescape_simulation.py instead.')
