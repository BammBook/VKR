import pandas as pd
import csv


file = '../model_data/csv_files/data2/tau_20.csv'

result = pd.read_csv('../model_data/csv_files/data2/tau_20.csv')
# print(result)


with open("../model_data/csv_files/data2/tau_20.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")
    count = 0
    for row in file_reader:
        if count == 0:
            print(f'Файл содержит столбцы: {", ".join(row)}')
        else:
            print(f'{row[0]}')
        count += 1
print(f'В файле {count} строк.')


