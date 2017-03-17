def freq_table(sentence):
    """Returns a table with occurences of each letter in the string. Case insensitive"""
    sentence = sentence.lower()
    sentence = sentence.replace(" ", "")
    letter_dict = {}
    for letter in sentence:
        letter_dict[letter] = letter_dict.get(letter, 0) + 1

    keys_list = list(letter_dict.keys())
    keys_list.sort()
    for key in keys_list:
        print("{0} {1}".format(key, letter_dict[key]))

freq_table("Test case of the first sentence in this function")