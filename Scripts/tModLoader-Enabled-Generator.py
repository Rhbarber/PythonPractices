import json
import os

# Get the current directory
current_directory = os.getcwd()

# Filter and retrieve all .tmod files in the current directory
tmod_files = [file.split(".")[0] for file in os.listdir(current_directory) if file.endswith(".tmod")]

# Write the list of elements to a JSON file with UTF-8 encoding and Ascii due to some mods having special characters
# such as Chinese letters.
with open("enabled.json", "w", encoding="utf-8") as json_file:
    json.dump(tmod_files, json_file, ensure_ascii=False, indent=4)

print("List of enabled .tmod files has been saved to 'enabled.json'.")
