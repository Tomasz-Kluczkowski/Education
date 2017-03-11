def filter(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        if len(text) <3:
            continue        # here we are filtering out all lines with words shorter than 3 letters

        # more logic for further filtering can be put in here
        outfile.write(text)

    infile.close()
    outfile.close()

filter("Grade 1 vocabulary.txt", "Grade 1 vocabulary_filtered.txt")