"""
Created By: Uee
Date: 27 October 2019
"""

import csv
import json
import os

from convert_to_type import adv_type_conversion

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


if __name__ == "__main__":
    print(
        """
        Option 1: Convert CSV to JSON 
        Option 2: Convert CSV to JSON, including a Unique Identifier. 
        Option 3: Convert CSV to JSON, including a Root Key. 
        Option 4: Convert CSV to JSON, including a Root Key and Unique Identifier. 
        """
    )

    option = input("Enter a Conversion Option 1, e.g. 1 for Option 1: ")

    extra_options = input("Do you want to view the Extra Options? Enter Y for Yes or N for No: ")

    if extra_options.lower() == "y":
        allow = input("\nAllow Empty Strings? Enter Y for Yes or N for No: ")
        allow_empty_strings = False if allow.lower() == "n" else True if allow == "y" else allow_empty_strings

        allow = input("Allow Null Values? Enter Y for Yes or N for No: ")
        allow_null_values = False if allow.lower() == "n" else True if allow.lower() == "y" else allow_null_values

    if option == "1":
        convert_csv_to_json(input("\nEnter a CSV Filename of Location: "),
                            input("Enter a Json Filename: "))

    elif option == "2":
        convert_csv_to_json_with_uid(input("\nEnter a CSV Filename or Location: "),
                                     input("Enter a Json Filename: "),
                                     input("Enter a CSV Column Tag: "))

    elif option == "3":
        convert_csv_to_json_with_root(input("\nEnter a CSV Filename or Location: "),
                                      input("Enter a Json Filename: "),
                                      input("Enter a name for the Root Key: "))

    elif option == "4":
        convert_csv_to_json_with_root_and_uid(input("\nEnter a CSV Filename or Location: "),
                                              input("Enter a Json Filename: "),
                                              input("Enter a name for the Root Key: "),
                                              input("Enter a CSV Column Tag: "))

    os.system("pause")
