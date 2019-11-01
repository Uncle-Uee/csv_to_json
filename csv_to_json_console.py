"""
Created By: Uee
Date: 29 October 2019
"""

import csv
import json
import sys

from csv_to_json import adv_type_conversion

allow_empty_strings = True
allow_null_values = True


def convert_csv_to_json(csv_path = "", json_path = "", allow_empty_strings = True, allow_null_values = True):
    """
    Convert a CSV to JSON
    :param csv_path: Path Location of the CSV file. This can just be the name of the CSV file if the CSV
     and the Program is in the same location.
    :param json_path: Path location where the Json File should be saved. This can just be the name of the Json File if
    wish to save the Json File in the same location of the program.
    :return:
    """
    try:
        data = []
        with open(csv_path, 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                for key in row.keys():
                    row[key] = adv_type_conversion(row[key], allow_empty_strings, allow_null_values)
                data.append(row)

        with open(json_path if json_path != "" else "parse.json", 'w') as jsonFile:
            jsonFile.write(json.dumps(data, indent = 4))

        print("Conversion Successful!")

    except Exception as error:
        print(error)


def convert_csv_to_json_with_uid(csv_path = "", json_path = "", column_tag = "", allow_empty_strings = True,
                                 allow_null_values = True):
    """
    Convert a CSV to JSON with Unique Identifier.
    :param csv_path: Path Location of the CSV file. This can just be the name of the CSV file if the CSV
     and the Program is in the same location.
    :param json_path: Path location where the Json File should be saved. This can just be the name of the Json File if
    wish to save the Json File in the same location of the program.
    :param column_tag: Column to use as a Unique Identifier
    :return:
    """
    try:
        data = {}
        with open(csv_path, 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                for key in row.keys():
                    row[key] = adv_type_conversion(row[key], allow_empty_strings, allow_null_values)
                key = row[column_tag]
                data[key] = row

        with open(json_path if json_path != "" else "parse.json", 'w') as jsonFile:
            jsonFile.write(json.dumps(data, indent = 4))

        print("Conversion Successful!")

    except Exception as error:
        print(error)


def convert_csv_to_json_with_root(csv_path = "", json_path = "", root_key = "", allow_empty_strings = True,
                                  allow_null_values = True):
    """
    Convert CSV to JSON with Root Key.
    :param csv_path: Path Location of the CSV file. This can just be the name of the CSV file if the CSV
     and the Program is in the same location.
    :param json_path: Path location where the Json File should be saved. This can just be the name of the Json File if
    wish to save the Json File in the same location of the program.
    :param root_key: Root Key name of the Json Data.
    :return:
    """
    try:
        data = []
        rooted_data = {}
        with open(csv_path, 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                for key in row.keys():
                    row[key] = adv_type_conversion(row[key], allow_empty_strings, allow_null_values)
                data.append(row)

        rooted_data[root_key] = data
        with open(json_path if json_path != "" else "parse.json", 'w') as jsonFile:
            jsonFile.write(json.dumps(data if root_key == "" else rooted_data, indent = 4))

        print("Conversion Successful!")

    except Exception as error:
        print(error)


def convert_csv_to_json_with_root_and_uid(csv_path = "", json_path = "", root_key = "", column_tag = "",
                                          allow_empty_strings = True, allow_null_values = True):
    """
    Convert a CSV to JSON with a Root Key and Unique Identifier.
    :param csv_path: Path Location of the CSV file. This can just be the name of the CSV file if the CSV
     and the Program is in the same location.
    :param json_path: Path location where the Json File should be saved. This can just be the name of the Json File if
    wish to save the Json File in the same location of the program.
    :param column_tag: Column to use as a Unique Identifier
    :param root_key: Root Key name of the Json Data.
    :return:
    """
    try:
        data = {}
        rooted_data = {}
        with open(csv_path, 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                for key in row.keys():
                    row[key] = adv_type_conversion(row[key], allow_empty_strings, allow_null_values)
                key = row[column_tag]
                data[key] = row

        rooted_data[root_key] = data
        with open(json_path if json_path != "" else "parse.json", 'w') as jsonFile:
            jsonFile.write(json.dumps(data if root_key == "" else rooted_data, indent = 4))

        print("Conversion Successful!")

    except Exception as error:
        print(error)


"""
The console version is still under development! Sorry for the inconvenience. 
"""
if __name__ == "__main__":
    if len(sys.argv) > 1:
        arguments = sys.argv[1:]

    for i in range(0, len(arguments)):
        arguments[i] = adv_type_conversion(arguments[i])
        print(arguments[i])
        print(type(arguments[i]))

    csv_location = arguments[0]
    json_location = arguments[1]

    convert_csv_to_json(csv_location, json_location)
