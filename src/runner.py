import csv
import os

from src import repeetcode

filename = "data.csv"


def run():
    data = repeetcode.load_data(filename)

    user_input = ''
    while user_input != 'q':
        print('\nInput an option:')
        user_input = input('[q]uit | [a]dd problem | [r]andom problem\n').lower()
        os.system('cls' if os.name=='nt' else 'clear')
        match user_input:
            case 'q': print('bye bye!')
            case 'a': repeetcode.add_problem(data)
            case 'r': repeetcode.random_problem(data)
            case _: print('Invalid input')


if __name__ == '__main__':
    run()