# this script renames all files in the directory images such that it replaces "_" with "-"
# and convers the text to lowercase

import os

# get the current working directory
path = os.getcwd()

# change the working directory to images

os.chdir(path + "/Images")

# get the current working directory
path = os.getcwd()

# get a list of all files in the directory
files = os.listdir(path)

# loop through the files
for file in files:
    # get the old file name
    old_file_name = file
    # get the new file name
    new_file_name = file.replace("_", "-").lower()
    # rename the file
    os.rename(old_file_name, new_file_name)
    print(f"{old_file_name} has been renamed to {new_file_name}")
