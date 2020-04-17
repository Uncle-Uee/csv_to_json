# CSV to Json
Convert a CSV to a JSON file.

## Getting Started
These instructions below will guide you on how to use and compile either the csv_to_json_gui or csv_to_json_console.

## Basic Console Use
The following instructions below will guide you on how to use the csv_to_json_console.py script through the command prompt or built as an executable.

### Command Line Arguments
    1. Simple Conversion:
    Command: "csv_to_json_console csv_file.csv parsed.json"
		- where csv_file.csv & parsed.json, are the locations to your csv file and the save location of 
		your json file.
		- if the files of the csv and the python executable or script are in the same place you can just use 
		the names of the files.

    2. Advanced Conversion with Unique Identifier:
	Command: "csv_to_json_console csv_file.csv parsed.json -c Column Tag"
		- where Column Tag, is the name of a Header Tag in the CSV File
	Output: Using State as the Unique Identifier Column
    {
        "Western Cape" : {
            "City" : "Cape Town",
            "Population" : "4.62 million"
        }
    }

    3. Advanced Conversion with Root:
	Command: "csv_to_json_console csv_file.csv parsed.json -r Root"
		- where Root, is a custom tag you enter.
	Output: Using a Root Tag where root = "States"
    {
        "States" : {
            "State" : "Western Cape"
            "City" : "Cape Town",
            "Population" : "4.62 million"
        }
    }

    4. Advanced Conversion with Root and UID:
	Command: "csv_to_json_console csv_file.csv parsed.json -c Column Tag -r Root"
	Output: Using a Root Tag and Column as Unique Identifier
	{
	    "States" : {
	        "Western Cape" : {
	            "City" : "Cape Town",
	            "Population" : "4.62 million"
	        }
	    }
	}

    5. Advanced Conversion with Flags:
	Command: "csv_to_json_console csv_file.csv parsed.json -nv"
		- where -nv, Replace all null values with Empty Strings

	Command: "csv_to_json_console csv_file.csv parsed.json -es"
		- where -es, Replace all empty strings with Null Values

	Command: "csv_to_json_console csv_file.csv parsed.json -es -nv"
		- where -nv, Replace all null values with Empty Strings
		- where -es, Replace all empty strings with Null Values

    6. Super Advanced Conversion:
	Command: "csv_to_json_console csv_file.csv parsed.json -c Column Tag -r Root -es -nv"
		- Note: you can include and exclude which ever optional arguments as you require.
		
## Basic UI Use
> Important: Make sure PyQT5 is installed. 
1. Run the csv_to_json_gui.py script or compile and run the executable version of it.
2. Select your CSV File
3. Select your Json Save Location
4. Additional arguments include
   1. Column Tag
   2. Root Tag
   3. Removal of Empty Strings and Null Values
5. Click Convert

## Build
Requirements:
```
PyQT5 -version 5.12.1
PyQT5-Tools
PyQT5-Sip
PyQT5-Stub -version 5.12.1
PyInstaller
```

You can convert the csv_to_json_console or csv_to_json_gui to an exe using the commands below.

With Icon:
```
pyinstaller --onefile --console --icon=croissant.ico csv_to_json_console.py
pyinstaller --onefile --console --icon=croissant.ico csv_to_json_gui.py
```

Without Icon:
```
pyinstaller --onefile --console csv_to_json_console.py
pyinstaller --onefile --console csv_to_json_gui.py
```
You replace croissant icon with any other icon you wish.
## License
This project is licensed under the MIT License - set the [LICENSE.md](LICENSE.md) file for details

## Authors
[Ubaidullah Effendi-Emjedi](https://www.linkedin.com/in/ubaidullah-effendi-emjedi-202494183/)