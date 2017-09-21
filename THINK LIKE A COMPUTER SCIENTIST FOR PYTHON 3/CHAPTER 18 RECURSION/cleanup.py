"""
11.Write a program named litter.py that creates an empty file named trash.txt in each subdirectory of a directory tree given the root of the tree as an argument (or the current directory as a default). Now write a program named cleanup.py that removes all these files.

Hint #1: Use the program from the example in the last section of this chapter as a basis for these two recursive programs. Because you’re going to destroy files on your disks, you better get this right, or you risk losing files you care about. So excellent advice is that initially you should fake the deletion of the files — just print the full path names of each file that you intend to delete. Once you’re happy that your logic is correct, and you can see that you’re not deleting the wrong things, you can replace the print statement with the real thing.

Hint #2: Look in the os module for a function that removes files.

myfile = open("test.txt", "w")
myfile.write("My first file written from Python\n")
myfile.write("---------------------------------\n")
myfile.write("Hello, World!\n")
myfile.close()

os.remove(path)

"""

import os

def get_dirlist(path):
    """ Return a sorted list of all entries in path.
    This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def remove_litter(path):
    """ Print recursive listing of contents of path """
    dirlist = get_dirlist(path)
    for file in dirlist:

        fullname = os.path.join(path, file)  # turn name into full pathname
        if os.path.isfile(fullname):
            if  file == "litter.txt":
                print("Deleting: {0}".format(fullname))
                os.remove(fullname)
        else:
            remove_litter(fullname)

remove_litter("C:\\Temp\\")