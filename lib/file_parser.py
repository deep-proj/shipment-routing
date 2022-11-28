import csv

def parse_file(filename: str):
    """Takes in a csv file, and creates a data matrix of the information"""
    file = csv.DictReader(filename)
    data = []
    for row in file:
        data.append(row)

    return data