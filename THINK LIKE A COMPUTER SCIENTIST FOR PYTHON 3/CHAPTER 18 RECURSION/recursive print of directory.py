import os

def get_dirlist(path):
    """ Return a sorted list of all entries in path.
    This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ""):
    """ Print recursive listing of contents of path """
    if prefix == "": #detect outermost call, print a heading
        print("folder listing for", path)
        prefix = "| "


    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix +f)    # print the line
        fullname = os.path.join(path, f)    # turn name into full pathname
        if os.path.isdir(fullname):
            print_files(fullname, prefix + "| ")

print_files("c:\\users\\")