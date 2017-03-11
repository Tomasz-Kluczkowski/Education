def number_lines(file):
    """ Read a file and number all lines then write the file """

    input_handle = open(file)
    output_handle = open("copy_of_{0}.txt".format(file), "w")

    line_counter = 0

    while True:
        line = input_handle.readline()
        if len(line) == 0:
            break
        line = "{0:>04} ".format(line_counter) + line
        line_counter += 1
        output_handle.write(line)


    input_handle.close()
    output_handle.close()

number_lines("Ex 1 read and write lines in reversed order.py")