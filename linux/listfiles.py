"""

>>> os.listdir('dir_path'): Return the list of files and directories present in a specified directory path.

--- LIST ALL FILES IN A DIRECTORY ---

Getting a list of files of a directory is easy as pie! Use the listdir() and isfile() functions of an os module to list all files of a directory. Here are the steps.

Import os module
This module helps us to work with operating system-dependent functionality in Python. The os module provides functions for interacting with the operating system.

Use os.listdir() function
The os.listdir('path') function returns a list containing the names of the files and directories present in the directory given by the path.

Iterate the result
Use for loop to Iterate the files returned by the listdir() function. Using for loop we will iterate each file returned by the listdir() function

Use isfile() function
In each loop iteration, use the os.path.isfile('path') function to check whether the current path is a file or directory. If it is a file, then add it to a list. This function returns True if a given path is a file. Otherwise, it returns False.


--- LIST ONLY FILES ---

import os

# folder path
dir_path = r'E:\\account\\'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
print(res)


--- LIST FILES & DIRECTORY ---

import os

# folder path
dir_path = r'E:\\account\\'

# list file and directories
res = os.listdir(dir_path)
print(res)











>>> os.walk('dir_path'): Recursively get the list all files in directory and subdirectories.

The os.walk() function returns a generator that creates a tuple of values (current_path, directories in current_path, files in current_path).

Note: Using the os.walk() function we can list all directories, subdirectories, and files in a given directory.

It is a recursive function, i.e., every time the generator is called, it will follow each directory recursively to get a list of files and directories until no further sub-directories are available from the initial directory.

For example, calling the os.walk('path') will yield two lists for each directory it visits. The first list contains files, and the second list includes directories.

from os import walk

# folder path
dir_path = r'E:\\account\\'

# list to store files name
res = []
for (dir_path, dir_names, file_names) in walk(dir_path):
    res.extend(file_names)
    #break to stop looking files recursively inside subdirectories
print(res)










>>> os.scandir('path'): Returns directory entries along with file attribute information.
It returns an iterator of os.DirEntry objects, which contains file names.

import os

# get all files inside a specific folder
dir_path = r'E:\\account\\'
for path in os.scandir(dir_path):
    if path.is_file():
        print(path.name)












>>> glob.glob('pattern'): glob module to list files and folders whose names follow a specific pattern.

The Python glob module, part of the Python Standard Library, is used to find the files and folders whose names follow a specific pattern.

For example, to get all files of a directory, we will use the dire_path/*.* pattern. Here, *.* means file with any extension.

import glob

# search all files inside a specific folder
# *.* means file name with any extension
dir_path = r'E:\account\*.*'
res = glob.glob(dir_path)
print(res)


# list from subdirectories, add recursive = True

import glob

# search all files inside a specific folder
# *.* means file name with any extension
dir_path = r'E:\demos\files_demos\account\**\*.*'
for file in glob.glob(dir_path, recursive=True):
    print(file)
    
    









>>> pathlib module to list files of a directory

From Python 3.4 onwards, we can use the pathlib module, which provides a wrapper for most OS functions.

Import pathlib module: Pathlib module offers classes and methods to handle filesystem paths and get data related to files for different operating systems.

Next, Use the pathlib.Path('path') to construct directory path

Next, Use the iterdir() to iterate all entries of a directory

In the end, check if a current entry is a file using the path.isfile() function

import pathlib

# folder path
dir_path = r'E:\\account\\'

# to store file names
res = []

# construct path object
d = pathlib.Path(dir_path)

# iterate directory
for entry in d.iterdir():
    # check if it a file
    if entry.is_file():
        res.append(entry)
print(res)

"""