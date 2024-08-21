from time import sleep

class UtilsGame:

    @staticmethod
    def slow_print(text: str) -> None:
        '''
        Print text letter by letter at slower speed.
        '''
        for letter in f'{text}\n':
            print(f'{letter}', end='', flush=True)
            sleep(0.03)

ug = UtilsGame()
ug.slow_print('Hello i am going there')

if __name__ == '__main__':
    print('Please run rs3.py instead.')
