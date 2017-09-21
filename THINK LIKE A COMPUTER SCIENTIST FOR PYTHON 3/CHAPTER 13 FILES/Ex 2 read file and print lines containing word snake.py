def print_with_snake(file):
    """ Read a file and print out only the lines containing substring snake """

    file_handle = open(file)

    while True:
        line = file_handle.readline()
        if len(line) == 0:
            break
        if "snake" in line:
            print(line, end = "")
        else:
            continue

    file_handle.close()

print_with_snake("snake test.txt")