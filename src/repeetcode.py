import csv
import random
import json
import os
from urllib.request import urlopen, Request


# shhhhhhhh
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
leetcode_api = 'https://leetcode.com/api/problems/algorithms/'

file_name = 'data.csv'

class RepeetCode:

    def __init__(self):
        self.data = []
        if not os.path.exists(file_name): # make if it doesnt exist
            with open(file_name, 'w'): pass
        else:
            with open(file_name, 'r', newline='') as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    print(row)
                    self.data.append([int(row[0]), row[1]])

        self.problems = {}
        leetcode_json_string = urlopen(Request(leetcode_api, headers=headers)).read().decode('utf-8')
        for problem in json.loads(leetcode_json_string)['stat_status_pairs']:
            self.problems[problem['stat']['frontend_question_id']] = {'name':       problem['stat']['question__title'],
                                                                      'url_slug':   problem['stat']['question__title_slug'],
                                                                      'difficulty': problem['difficulty']['level']}

    def add_problem(self):
        problem_number = input('Enter problem number: ')
        if not problem_number.isdigit() or int(problem_number) not in self.problems:
            print('Invalid problem number!')
            return
        
        problem_number_int = int(problem_number)
        
        if problem_number_int in [item[0] for item in self.data]:
            print('Problem already added!')
            return

        problem_hint = input('Enter your hint/reminder for the problem: ')

        self.data.append((problem_number_int, problem_hint))
        with open(file_name, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([problem_number, problem_hint])
        return


    def random_problem(self):
        difficulties = ['Easy', 'Medium', 'Hard']

        problem_number, problem_hint = random.choice(self.data)
        problem_name = self.problems[problem_number]['name']
        problem_url_slug = self.problems[problem_number]['url_slug']
        problem_difficulty = difficulties[self.problems[problem_number]['difficulty'] - 1]

        problem_url = f'https://leetcode.com/problems/{problem_url_slug}/'
        print(f'The problem is:\n\n{problem_number}. {problem_name}\nDifficulty: {problem_difficulty}\n{problem_url}\n')

        need_hint = ''
        while need_hint != 'y' and need_hint != 'n':
            need_hint = input('Need reminder? (y/n)')
            match need_hint:
                case 'y': print(f'Reminder: {problem_hint}')
                case 'n': return
                case _: print('Invalid input')

        return