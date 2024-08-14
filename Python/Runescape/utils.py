'''

Responsible script to make game utils.
Import time to slowdown printed text.

'''
import time

class Utils:
    '''

    Game utils. 
    
    '''

    @staticmethod
    def slow_txt(text) -> None:
        '''

        Print the text slower for a better game experience. 
        Flush=True = Write letter by letter to the terminal.
        
        '''
        for letter in text:
            print(letter, end='', flush=True)
            time.sleep(0.03) # Change for faster/slower speed.

    @staticmethod
    def check_bag(character) -> str:
        '''
        
        Check items in character bag.
        
        '''
        bag_items: str = ''
        for item in character.bag:
            bag_items += f'{item["quantity"]}x {item["item name"]}\n'
        util.slow_txt(f'\n{character.name} bag:\n{bag_items}')
        return bag_items

    @staticmethod
    def drop(mob, char) -> None:
        '''
        
        Drop items from monster and add it to character bag.
        
        '''
        for m_item in mob.bag:
            for p_item in char.bag:
                if m_item['item name'] in p_item['item name']:
                    p_item['quantity'] += m_item['quantity']
                    break
                if m_item not in char.bag:
                    char.bag.append(m_item)
                    break

    @staticmethod
    def lvl_up(char, xp: int) -> None:
        ''' Gain lvl on a specific skill. '''
        char.hp_lvl += xp

    @staticmethod
    def xp_up(char, xp: int) -> None:
        ''' Gain xp on specific skill. '''
        char.hp_xp += xp

util = Utils()

if __name__ == '__main__':
    print('please run runescape_simulation.py instead.')
