def filter(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    # sings_to_remove = ["'", "."]
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        if len(text) < 4 or  "'"  in text or "." in text:
            continue        # here we are filtering out all lines with words shorter than 3 letters
        text = text.replace("*", "")
        text = text.replace(" ", "")
        text = text.lower()

        outfile.write(text)

    infile.close()
    outfile.close()

for i in range(1, 6):
    filter("Grade " + str(i) + " vocabulary.txt", "Grade " + str(i) + " vocabulary_filtered.txt")