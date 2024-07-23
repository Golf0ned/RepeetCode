import csv
import os

from src import repeetcode

filename = "data.csv"


def run():
    data = []
    with open(filename, newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            data.append(row)

    user_input = ''
    while user_input != 'q':
        print('Input an option:')
        user_input = input('[q]uit | [a]dd problem | [r]andom problem\n').lower()
        os.system('cls' if os.name=='nt' else 'clear')
        match user_input:
            case 'q': print('bye bye!')
            case 'a': repeetcode.add_problem()
            case 'r': repeetcode.random_problem()
            case _: print('Invalid input')


if __name__ == '__main__':
    run()