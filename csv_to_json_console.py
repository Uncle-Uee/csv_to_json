import csv
import json
import argparse
import os

from convert_to_type import adv_type_conversion

# Initialize Argument Parser
parser = argparse.ArgumentParser()

# Required Arguments.
parser.add_argument("CSV", help = "CSV Filename or Path Location.", type = str)
parser.add_argument("JSON", help = "JSON Filename or Path Location.", type = str)

# Optional Arguments.
parser.add_argument("-c", "--column", help = "CSV Column Tag.", type = str)
parser.add_argument("-r", "--root", help = "Root Key", type = str)
parser.add_argument("-es", "--empty_string", action = "store_false", help = "Do not Allow Empty Strings.")
parser.add_argument("-nv", "--null_value", action = "store_false", help = "Do not Allow Null Values.")


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
HOW TO USE:
The following dialog is a set of instructions on how to use the csv_to_json_console.py script
through the command prompt or built as an executable.


BUILD EXECUTABLE (PyInstaller):
pyinstaller --onefile --console csv_to_json_console.py

USE COMMAND LINE ARGUMENTS:
CSV and JSON are compulsory arguments and respectively are the path locations of the csv and json files.


Examples:
Simple Conversion:
	csv_to_json_console csv_file.csv parsed.json
		- where csv_file.csv & parsed.json, is the location of your csv file otherwise just the name 
			of the csv file e.g. "cities.csv" if its in the same location as the executable or script.
			The same can be done with the json file save location. 

Advanced Conversion with UID:
	csv_to_json_console csv_file.csv parsed.json -c Column Tag
		- where Column Tag, is the name of a Header Tag in the CSV File

Advanced Conversion with Root:
	csv_to_json_console csv_file.csv parsed.json -r Root
		- where Root, is the name of the Root Key

Advanced Conversion with Root and UID:
	csv_to_json_console csv_file.csv parsed.json -c Column Tag -r Root

Advanced Conversion with Flags:
	csv_to_json_console csv_file.csv parsed.json -nv
		- where -nv, Replace all null values with Empty Strings

	csv_to_json_console csv_file.csv parsed.json -es
		- where -es, Replace all empty strings with Null Values

	csv_to_json_console csv_file.csv parsed.json -es -nv
		- where -nv, Replace all null values with Empty Strings
		- where -es, Replace all empty strings with Null Values


Super Advanced Conversion:
	csv_to_json_console csv_file.csv parsed.json -c Column Tag -r Root -es -nv
		- Note: you can include and exclude which ever optional arguments as you require.

"""

if __name__ == "__main__":
	arguments = parser.parse_args()

	csv_location = arguments.CSV
	json_location = arguments.JSON

	allow_empty_strings = arguments.empty_string
	allow_null_values = arguments.null_value

	if arguments.column != None and arguments.root != None:
		convert_csv_to_json_with_root_and_uid(csv_location, json_location, arguments.root, arguments.column,
		                                      allow_empty_strings, allow_null_values)
	elif arguments.column != None:
		convert_csv_to_json_with_uid(csv_location, json_location, arguments.column, allow_empty_strings,
		                             allow_null_values)
	elif arguments.root != None:
		convert_csv_to_json_with_root(csv_location, json_location, arguments.root, allow_empty_strings,
		                              allow_null_values)
	else:
		convert_csv_to_json(csv_location, json_location, allow_empty_strings, allow_null_values)
