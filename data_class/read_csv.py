import csv


def read_csv(filepath, filename):

    output_data = []

    with open("../model_data/csv_files/" + filepath + filename + ".csv", encoding='utf-8') as row_file:

        file_reader = csv.reader(row_file, delimiter=",")
        count = 0

        for row in file_reader:
            if count == 0:
                data_len = len(row)
                for i in range(data_len):
                    output_data.append([])

            else:
                for i in range(data_len):
                    output_data[i].append(float(row[i]))
            count += 1

    return output_data
