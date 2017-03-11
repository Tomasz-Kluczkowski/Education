def filter(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        if text[0] == "#":
            continue        # here we are filtering out all lines containing # sign at the index 0

        # more logic for further filtering can be put in here
        outfile.write(text)

    infile.close()
    outfile.close()

filter("input.txt", "output.txt")