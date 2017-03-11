def remove_number_lines(file):
    """ Read a file and remove line numbers then write the file """

    input_handle = open(file)
    output_handle = open("{0}_line_nos_removed.txt".format(file), "w")

    while True:
        line = input_handle.readline()
        if len(line) == 0:
            break
        line = line[5:]             # remove first 5 characters of every line where the line number sits
        output_handle.write(line)   # write the unnumbered line into the copy file


    input_handle.close()
    output_handle.close()

remove_number_lines("copy_of_Ex 1 read and write lines in reversed order.py.txt")