# import os

import repeetcode as rc

def run():
    repeetcode = rc.RepeetCode()

    user_input = ''
    while user_input != 'q':
        print('\nInput an option:')
        user_input = input('[q]uit | [a]dd problem | [r]andom problem\n').lower()
        # os.system('cls' if os.name=='nt' else 'clear')
        match user_input:
            case 'q': print('bye bye!')
            case 'a': repeetcode.add_problem()
            case 'r': repeetcode.random_problem()
            case _: print('Invalid input')


if __name__ == '__main__':
    run()