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
        util.slow_txt(
            f'\n{character.name} bag:\n{bag_items}'
            )
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
    def xp_up(char, skill: str, mob) -> None:
        '''
        Upgrade character xp using a list of tuples. 

        List of xp in skills (3 elements given): 
        1st: skill = name 
        2nd: character xp = c_xp
        3rd: monster given xp = m_xp

        '''
        xp_list = [
            ('hp', 'health_xp', 'health_xp'),
            ('atk', 'attack_xp', 'combat_xp'),
            ('str', 'strength_xp', 'combat_xp'),
            ('def', 'defense_xp', 'combat_xp'),
        ]

        for name, c_xp, m_xp in xp_list:
            if skill == name:
                # Update the total xp before setting it as an attribute.
                update = getattr(char.combat_skills, c_xp) + getattr(mob.xp, m_xp)
                setattr(char.combat_skills, c_xp, update)
                break
        else:
            print(f"Unknown skill: {skill}")

util = Utils()

if __name__ == '__main__':
    print('please run runescape_simulation.py instead.')
