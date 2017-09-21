'''
Write a function that removes all occurrences of a substring from another string:
1
2
3
4
test(remove("an", "banana") == "bana")
test(remove("cyc", "bicycle") == "bile")
test(remove("iss", "Mississippi") == "Missippi")
test(remove("eggs", "bicycle") == "bicycle")
'''


def remove_all_substrings(text,substring):
    """remove all substring occurences in string text"""

    ix = 0

    while text.find(substring,ix) != -1:

            ix = text.find(substring,ix)
            text = text[0:ix]+text[ix+len(substring):] #this slices out text without occurence of the substring

    return text


print(remove_all_substrings('Mississippi','iss'))
print(remove_all_substrings('bicycle','cyc'))
print(remove_all_substrings('doladowanie dodawania do dodatku doroslych','do'))
print(remove_all_substrings('bicycle','eggs'))
