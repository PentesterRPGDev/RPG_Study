from item import coins, bronze_scimitar
from monster import goblin, spider
from player import player
from utils_bag import Bag

player.bag.append(coins)
player.bag.append(bronze_scimitar)
print(player.bag)
player.bag.remove(coins)
print(player.bag)


if __name__ == '__main__':
    print('Adventure starts.')
