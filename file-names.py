# Returns text file on Desktop with list of file names. Python2.7

import os

folder_path = '/Users/dunnjt/Desktop/CODE'
folder_path = raw_input('\nWhat folder do you want scanned? ').strip()

contents = os.listdir(folder_path)
for item in contents:
    if item == '.DS_Store':
        contents.remove(item)

location = '/Users/dunnjt/Desktop'
os.chdir(location)
with open('file_names.txt', 'w') as fin:
    fin.write(folder_path + '\n')
    fin.write(str(len(contents)) + ' items\n\n')
    for line in contents:
        fin.write(line)
        fin.write('\n')

print('\nCOMPLETE\n')
