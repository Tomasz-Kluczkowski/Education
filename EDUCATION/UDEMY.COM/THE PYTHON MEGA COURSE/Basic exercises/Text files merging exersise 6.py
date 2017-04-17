# Coding Exercise 6: Merging Text Files
# Section 6, Lecture 53
# Here is a tricky exercise.
#
# Please download the ZIP file in the Resources and unzip it in a folder.
#
# Then create a script that merges the three text files into a new text file containing the text of all three files.
#  The filename of the merged text file should contain the current timestamp down to the millisecond level.
#  E.g. "2016-06-01-13-57-39-170965.txt".
#
# You have some tips in the next lecture and the solution in the lecture after that.
#
# Resources for this lecture
#  Sample Files.zip
import glob2

def merge_text(source_list):
    """Merge text from source into destination files
    The output file is named using current date & time"""
    import datetime
    destination = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
    output_file = open(destination + ".txt", "a")
    for source in source_list:
        with open(source, "r") as input_file:
            content = input_file.read()
            output_file.write(content + "\n")
    output_file.close()

source_list = glob2.glob("file?.txt")
merge_text(source_list)
