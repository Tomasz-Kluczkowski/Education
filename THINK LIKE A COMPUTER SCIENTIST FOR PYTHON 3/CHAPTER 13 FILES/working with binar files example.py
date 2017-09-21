f = open("somefile.zip", "rb")
g = open("thecopy.zip", "wb")

while True:
    buf = f.read(1024)  # we are dividing the file into 1024 byte chunks to be able to check for end of file
    if len(buf) == 0:
        break
    g.write(buf)        # copy chunk of original file somefile.zip into thecopy.zip

f.close()
g.close()
