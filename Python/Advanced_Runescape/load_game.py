import pandas as pd

from monster import Monster, MonsterInfo, MonsterSkills, MonsterExp

class LoadGame:
    def __init__(self) -> None:
        self.monsters: list = []
        self.items: list = []
        self.players: list = []

    def m_creator(self):
        '''
        Monster creator
        Reads monster data from monster_data.csv.
        From data create monster objects.
        Store monsters inside a list.
        '''
        monster_df = pd.read_csv('csv/monster_data.csv')
        for index, row in monster_df.iterrows():
            monster = Monster(
                MonsterInfo(
            row['name'], row['examine'], row['membership']),
                MonsterSkills(
            row['health'], row['attack'], row['strength'], row['defense']),
                MonsterExp(
            row['health_xp'], row['combat_xp'])
            )
            self.monsters.append(monster)

loadgame = LoadGame()
loadgame.m_creator()
goblin = loadgame.monsters[0]
print(goblin)
