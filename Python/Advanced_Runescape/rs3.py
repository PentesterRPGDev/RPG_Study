from item import coins, bronze_scimitar
from monster import goblin, spider
from utils_bag import Bag

Bag.append(goblin, coins, 10)
Bag.append(spider, coins, 100)
Bag.append(goblin, bronze_scimitar, 1)
print(goblin.bag)
print(spider.bag)

if __name__ == '__main__':
    print('Adventure starts.')
