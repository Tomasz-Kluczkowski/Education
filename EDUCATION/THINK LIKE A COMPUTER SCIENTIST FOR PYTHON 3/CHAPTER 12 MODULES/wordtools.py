from unit_testing import test
import string

def myreplace(old, new, s):
    """ Replace all occurences of old with new in s. """

    s = s.split()
    s = " ".join(s)

    return new.join(s.split(old))


def cleanword(s):
    """ Removes punctuation from string s and returns s """
    word = ""

    for letter in s:
        if letter not in string.punctuation:
            word += letter

    return word


def has_dashdash(s):
    """ Detect if string s contains double dash """
    return "--" in s


def extract_words(s):
    """ Split string into words, remove whitespace and punctuation """

    if has_dashdash(s):
        s = myreplace("--"," ", s)

    s = s.lower().split()
    word_list = []

    for word in s:

        word_list.append(cleanword(word))

    return word_list


def wordcount(word, word_list):
    """ Counts how many time word is contained in word_list """

    count = 0

    for item in word_list:

        if item == word:
            count += 1

    return count


def wordset(word_list):
    """ Returns a list of alphabetically ordered unique words in the word_list """

    unique_words = []

    for word in word_list:

        if word not in unique_words:
            unique_words.append(word)

    unique_words.sort()

    return unique_words


def longestword(word_list):
    """ Returns the lenght of a longest word in the word_list. """

    longest = 0

    for word in word_list:

        if len(word) > longest:
            longest = len(word)

    return longest


test(myreplace(",", ";", "this, that, and some other thing"), "this; that; and some other thing")
test(myreplace(" ", "**", "Words will now      be  separated by stars."), "Words**will**now**be**separated**by**stars.")

test(cleanword("what?"),"what")
test(cleanword("'now!'"),"now")
test(cleanword("?+='w-o-r-d!,@$()'"),"word")


test(has_dashdash("distance--but"), True)
test(not has_dashdash("several"), True)
test(has_dashdash("spoke--"), True)
test(has_dashdash("distance--but"), True)
test(not has_dashdash("-yo-yo-"), True)


test(extract_words("Now is the time!  'Now', is the time? Yes, now."), ['now','is','the','time','now','is','the','time','yes','now'])
test(extract_words("she tried to curtsey as she spoke--fancy"), ['she','tried','to','curtsey','as','she','spoke','fancy'])


test(wordcount("now", ["now","is","time","is","now","is","is"]),2)
test(wordcount("is", ["now","is","time","is","now","the","is"]),3)
test(wordcount("time", ["now","is","time","is","now","is","is"]),1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]),0)


test(wordset(["now", "is", "time", "is", "now", "is", "is"]), ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]), ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]), ["a", "am", "are", "be", "but", "is", "or"])


test(longestword(["a", "apple", "pear", "grape"]),5)
test(longestword(["a", "am", "I", "be"]),2)
test(longestword(["this","supercalifragilisticexpialidocious"]),34)
test(longestword([ ]),0)



