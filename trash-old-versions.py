# trash older pdf graphic plan versions.

import os
import time
from pprint import pprint as pp
import logging
import json
import shutil

# Configure logger.
logging.basicConfig(filename='trash-logger.txt',
                            format='%(asctime)s    %(message)s',
                            filemode='w')

# Create logging object.
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def main():
    trash_folder = create_trash()
    folder_path = search_folders()
    purge_list = create_pdf_list(folder_path)
    move_to_trash(trash_folder, purge_list)


def create_trash():
    # create trash folder on desktop. That folder can be deleted manually.
    trash_folder = "/Users/dunnjt/Desktop/TRASH"
    try:
        os.mkdir(trash_folder)
        logger.info('Made trash folder.')
        print('=== Made trash folder. ===\n')
        
    except OSError:
        logger.info('Trash directory already exists.')
        print('=== Trash folder already exists. ===\n')
    return trash_folder
    

def search_folders():
    # search in folders recursively.
    # folder_path = raw_input('Drag in which folder to scan: ')
    folder_path = "/Users/dunnjt/Desktop/PDFs"
    logger.info('Folder worked: '+ folder_path)
    return folder_path

def create_pdf_list(folder_path): # Returns list minus last modified pdf.
    files = os.listdir(folder_path)
    pdf_files = [] 
    for file in files: # Remove files that are not PDFs.
        if ".pdf" in file:
            pdf_files.append(os.path.join(folder_path, file))
        else:
            pass
    
    pdf_files.sort(reverse = False, key=modified_date)
    logging.info('PDF Keeping: ' + pdf_files[-1])
    pdf_files.pop()
    logging.info('Purging: ' + str(len(pdf_files)) + ' files.')
    logging.info('PDF Purge List: ' + json.dumps(pdf_files))

    return pdf_files

def modified_date(file): # Key to sort by modified date.
    return os.path.getmtime(file)



    # root_name = pdf_files[-1][0:-7]

def move_to_trash(trash_folder, purge_list):
    logger.info('Moving list to trash folder.')
    for i in purge_list:
        shutil.move(i, trash_folder)
    
    logger.info('Move complete.')

if __name__ == "__main__":
    main()