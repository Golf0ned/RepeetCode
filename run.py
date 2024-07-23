import csv
import sys

filename = "data.csv"

print('Reading data...', end='')
data = []
with open(filename, newline='') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        data.append()
print('done!')
