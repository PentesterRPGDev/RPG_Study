from os import system

class NPC:
    def __init__(self, name: str, mira: bool) -> None:
        self.name = name
        self.mira = mira
    
    def __str__(self) -> str:
        return f'{self.name} nasceu mira: {self.mira}\n'
    
    def roubar(self) -> str:
        if self.mira == True:
            print(
                f'{self.name} says:\nDame o telemóvel já!\n'
                )
        else:
            print(
                f'{self.name} says:\nEstas seguro.\n'
                )

if __name__ == '__main__':
    system('clear')
    npc1 = NPC('Cravo', False)
    npc2 = NPC('Rodrigo', True)
    print(npc1)
    print(npc2)
    npc1.roubar()
    npc2.roubar()