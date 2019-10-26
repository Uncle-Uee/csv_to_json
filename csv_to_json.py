import csv
import json
import os

from convert_to_type import type_conversion


def convert_csv_to_json(csv_path = "", json_path = "parsed.json"):
    """
    Convert a CSV to JSON
    :return:
    """
    try:
        values = []
        with open(csv_path, 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                for key in row.keys():
                    row[key] = type_conversion(row[key])
                values.append(row)

        with open(json_path, 'w') as jsonFile:
            jsonFile.write(json.dumps([row for row in values], indent = 4))

    except Exception as error:
        print(error)


if __name__ == "__main__":
    convert_csv_to_json(input("Enter a CSV Filename or Location: "), input("Enter a Json Filename: "))
    os.system("pause")
