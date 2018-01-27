import csv


def csv_iterator(func, file, column):
    """
    Generator
    Takes string for csv file location,
    opens file and loads into csv reader object,
    for each row in csv object, apply function to the row and return the result
    """

    with open(file, newline='') as f:
        if column.isdigit():
            reader = csv.reader(f)
            column = int(column)
        else:
            reader = csv.DictReader(f)

        for row in reader:
            yield func(row[column])
