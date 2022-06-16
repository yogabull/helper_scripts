# rename
import os

directory = raw_input("Enter a directory")
# directory = "/Users/dunnjt/Documents/JOBS/21-12-03_RIMS-Wellness/ART/fixture"
print(directory)
os.chdir(directory)
files = os.listdir(directory)

rename   = raw_input("Enter new name: ")
count = 5

for file in files:
    if 'multi' in file:
        print('PASSING: ', file)
        pass
    count += 1
    ext = '.jpg'
    newName = rename + '-' + str(count) + ext
    
    # print(file, newName)
    os.rename(file, newName)


# print(sorted(os.listdir(directory)))