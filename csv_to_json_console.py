"""
Created By: Ubaidullah Effendi-Emjedi
Date: 27 October 2019
"""

from argparse import ArgumentParser

from src.converters.csv_to_json import *

# Initialize Argument Parser
parser = ArgumentParser()

# Required Arguments.
parser.add_argument("CSV", help="CSV Filename or Path Location.", type=str)
parser.add_argument("JSON", help="JSON Filename or Path Location.", type=str)

# Optional Arguments.
parser.add_argument("-c", "--column", help="CSV Column Tag.", type=str)
parser.add_argument("-r", "--root", help="Root Key", type=str)
parser.add_argument("-es", "--empty_string", action="store_false", help="Do not Allow Empty Strings.")
parser.add_argument("-nv", "--null_value", action="store_false", help="Do not Allow Null Values.")

if __name__ == "__main__":
    arguments = parser.parse_args()

    csv_location = arguments.CSV
    json_location = arguments.JSON

    allow_empty_strings = arguments.empty_string
    allow_null_values = arguments.null_value

    if arguments.column is not None and arguments.root is not None:
        convert_csv_to_json_with_root_and_uid(csv_location, json_location, arguments.root, arguments.column,
                                              allow_empty_strings, allow_null_values)
    elif arguments.column is not None:
        convert_csv_to_json_with_uid(csv_location, json_location, arguments.column, allow_empty_strings,
                                     allow_null_values)
    elif arguments.root is not None:
        convert_csv_to_json_with_root(csv_location, json_location, arguments.root, allow_empty_strings,
                                      allow_null_values)
    else:
        convert_csv_to_json(csv_location, json_location, allow_empty_strings, allow_null_values)
