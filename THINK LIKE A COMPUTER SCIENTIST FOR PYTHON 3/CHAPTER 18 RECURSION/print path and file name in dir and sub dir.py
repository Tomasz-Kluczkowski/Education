import os

def get_dirlist(path):
    """ Return a sorted list of all entries in path.
    This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path):
    """ Print recursive listing of contents of path """
    dirlist = get_dirlist(path)
    for f in dirlist:

        fullname = os.path.join(path, f)    # turn name into full pathname
        if os.path.isfile(fullname):
            print(fullname)
        else:
            print_files(fullname)

print_files("C:\\Miele_Service")
