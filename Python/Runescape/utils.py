''' Responsible script to make game utils. '''
class Utils:
    ''' Game utils. '''

    @staticmethod
    def check_bag(character) -> str:
        ''' Check items in character bag. '''
        bag_items: str = ''
        for item in character.bag:
            bag_items += f'{item["quantity"]}x {item["item name"]}\n'
        print(
            f'\n{character.name} bag:\n{bag_items}'
            )
        return bag_items

    @staticmethod
    def drop(mob, char) -> None:
        ''' Drop items from monster and add it to character bag. '''
        print(
            f'{mob.name} dropped:'
        )
        for m_item in mob.bag:
            for p_item in char.bag:
                if m_item['item name'] in p_item['item name']:
                    p_item['quantity'] += m_item['quantity']
                    print(
                        f'{m_item["quantity"]}x {m_item["item name"]}.'
                    )
                    break
                if m_item not in char.bag:
                    print(
                        f'{m_item["quantity"]}x {m_item["item name"]}.'
                    )
                    char.bag.append(m_item)
                    break

util = Utils()

if __name__ == '__main__':
    print('please run rs3.py instead.')
