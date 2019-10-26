# CSV to Json
Convert a CSV file to a JSON file

# How to
1. Run the python script csv_to_json.py
2. Enter a path location (c:/Users/Alias/Desktop/cities.csv) of the csv file you wish to convert to json. Otherwise if you place your csv file and the source code within the same directory you only need to specify the name of the csv file (cities.csv).
3. Enter a path location to where the Json File should be saved to or Enter a just a Json filename to save the Json file in the same location as the Script.
4. Done!


# Misc
You can convert the csv_to_json.py to an exe. I used PyInstaller and the following command to get an exe on Windows 10. 
pyinstaller --onefile --console csv_to_json.py
