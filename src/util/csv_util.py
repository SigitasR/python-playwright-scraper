import csv
import time
from dataclasses import asdict

from src.dataclasses.ProductData import ProductData


def write_to_file(data: [ProductData]):
    columns: [] = asdict(data[0]).keys()
    file_name = f'output-{time.time_ns()}.csv'
    try:
        with open(file_name, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, columns)
            writer.writeheader()
            for row in data:
                writer.writerow(asdict(row))
    except IOError as err:
        print(err)
