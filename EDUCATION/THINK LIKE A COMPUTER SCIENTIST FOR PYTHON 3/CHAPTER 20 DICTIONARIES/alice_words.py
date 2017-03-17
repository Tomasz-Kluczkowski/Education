import string

file_handle = open("Alice_in_wonderland.txt", "r", encoding="UTF8")
word_list = file_handle.read()
file_handle.close()

word_dict = {}
word_list = word_list.lower()
in_chars = string.ascii_letters + string.punctuation
out_chars = string.ascii_letters + (" " * 32)
translation = word_list.maketrans(in_chars, out_chars)
word_list = word_list.translate(translation)

word_list = word_list.split()
word_list.sort()

# Count occurences of each word in the book.
for word in word_list:
    word_dict[word] = word_dict.get(word, 0) + 1

keys_list = list(word_dict.keys())
keys_list.sort()

print("{0:<18}{1}".format("Word", "Count"))
print("{0:=<23}".format("="))
for key in keys_list:
    print("{0:<18}{1:>5}".format(key, word_dict[key]))

print("The longest word in the book is: {0}".format(max(keys_list, key = len)))
print("It's length is: {0} letters.".format(len(max(keys_list, key = len))))