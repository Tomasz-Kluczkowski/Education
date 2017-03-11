def reverse_lines(oldfile, newfile):
    """ Reads all lines of the oldfile and writes a newfiles with lines in reversed order. """
    input_handle = open(oldfile)
    line_list = input_handle.readlines()  # read all lines and create a list of them
    input_handle.close()

    if "\n" not in line_list[len(line_list)-1]: # check if there is a next line character after the last line to avoid joining lines after reversing order of the list
        line_list[len(line_list)-1] += "\n"     # add missing next line character to the last element of the list

    line_list.reverse()             # reverse order of lines

    output_handle = open(newfile, "w")

    for line in line_list:
        output_handle.write(line)

    output_handle.close()


reverse_lines("friends.txt", "friends_reversed.txt")