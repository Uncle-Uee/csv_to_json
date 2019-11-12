# CSV to Json
Convert a CSV file to a JSON file

# Basic Console Use
1. Run the python script csv_to_json.py
2. Choose an Option: 1, 2, 3 or 4
3. Enter Y or N to see additional options.
3.1 Enter Y or N to allow empty strings or null values in your output json file.
4. Enter a path location (c:/Users/Alias/Desktop/cities.csv) of the csv file you wish to convert to json. Otherwise if you place your csv file and the source code within the same directory you only need to specify the name of the csv file (cities.csv).
5. Enter a path location to where the Json File should be saved to or Enter a just a Json filename to save the Json file in the same location as the Script.
6. Conversion Complete! I hope :)

# Basic GUI Use
1. Open the GUI
2. Choose your CSV file.
3. Choose you Json Output File save Location.
4. Set you additional options: Allow Empty Strings, Allow Null Values, Choose a CSV Column as a Unique Identifier, Root Data.
5. Click Convert, and everything should be OOOOOK!

# Build an Executable
Requirements
PyQT5 -version 5.12.1
PyQT5-Tools
PyQT5-Sip
PyQT5-Stub -version 5.12.1
PyInstaller

Additionally you are required to copy the "csv_to_json.py" and "convert_to_type.py" to the "Python/Scripts/" folder as well. I ran into problems with the required functions in those scripts not being found once an executable was made.
However, if you can find a solution to that problem please let me know, I will definitely appreciate it.

You can convert the csv_to_json.py, csv_to_json_console and csv_to_json_gui to an exe using the commands below. 
pyinstaller --onefile --console --icon=croissant.ico csv_to_json.py
pyinstaller --onefile --console --icon=croissant.ico csv_to_json_gui.py
pyinstaller --onefile --console --icon=croissant.ico csv_to_json_console.py

# Pending Features
1. Complete the csv_to_json_console with full range of possible accepted arguments.

# Notes
The csv_to_json.py and the convert_to_type.py are the core scripts. These scripts are all you need to do your csv to json conversion. 
You can copy these scripts together and paste them anywhere you want and you will be able to use there functions. It would be ideal to copy them to "Python/Scripts" folder so that you can use there functions from within any of your other python projects.
