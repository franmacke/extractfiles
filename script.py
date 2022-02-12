import shutil
from pathlib import Path
import os
import sys

DIRECTORY = Path.cwd()
SOURCE = os.path.join(DIRECTORY, 'source')
EXTENSION = '.jpg'
DEF_TARGET = os.path.join(DIRECTORY, 'target/')

def algorithm(directory: str):
    if os.path.isdir(directory):
        children = get_children(directory)
        for child in children:
            algorithm(child)                
    else:
        if directory.endswith(EXTENSION):
            copy_to_target(directory)
    
def get_children(directory):
    dir_list = [os.path.join(directory, child) for child in os.listdir(directory)]
    return dir_list

def copy_to_target(path: str):
    shutil.copy(path, DEF_TARGET)

def main(args):
    if len(args) == 0:
        raise "Missing source directory."
    if not os.path.isdir(args[0]):
        raise f"{args[0]} is not a directory."
    initialize()
    algorithm(args[0])

def initialize():
    if not os.path.isdir(DEF_TARGET):
        os.mkdir(DEF_TARGET)

if __name__ == "__main__":
    main(sys.argv[1:])