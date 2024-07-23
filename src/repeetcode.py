import csv

def load_data(filename):
    data = []
    # a+ to generate file if not existing
    with open(filename, 'a+', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            data.append(row)
    return data

def add_problem(data):
    print('add_problem')

def random_problem(data):
    print('random_problem')