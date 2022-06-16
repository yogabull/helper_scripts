"""A quick way to record output/variables to a file for reference. Python3.9"""
import json
import os

def ref(payload):
    """Appends payload to a reference file."""
    if payload != str:
        payload = json.dumps(payload)
    with open ('reference.txt', 'a', encoding='utf-8') as fin:
        message = input('ENTER MESSAGE: ') # Add note about payload.
        new_message = message + '\n'
        line = '\n-------------\n'
        fin.writelines('\n')
        fin.writelines(new_message)
        fin.writelines(payload)
        fin.write(line)

def get_names():
    """Script writes file names in a directory to a text file.
    -- Drag directory to terminal window when prompted for folder to scan."""
    folder_path = os.getcwd()
    folder_path = input("\nWhat folder do you want recorded? (Drag folder into terminal) ").strip()

    contents = os.listdir(folder_path)
    for item in contents:
        if item == '.DS_Store':
            contents.remove(item)

    location = '/Users/dunnjt/Desktop'
    os.chdir(location)
    with open('file_names.txt', 'w', encoding='utf-8') as fin:
        fin.write(folder_path + '\n')
        fin.write(str(len(contents)) + ' items\n\n')
        for line in contents:
            fin.write(line)
            fin.write('\n')
