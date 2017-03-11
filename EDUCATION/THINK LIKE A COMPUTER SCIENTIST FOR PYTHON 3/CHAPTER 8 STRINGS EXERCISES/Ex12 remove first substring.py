'''
Write a function that removes the first occurrence of a string from another string:
1
2
3
4
test(remove("an", "banana") == "bana")
test(remove("cyc", "bicycle") == "bile")
test(remove("iss", "Mississippi") == "Missippi")
test(remove("eggs", "bicycle") == "bicycle")
'''


def remove_substring(text,substring):
    """count how many times substring occurs in string text"""

    ix = 0

    if text.find(substring,ix) != -1:
        ix = text.find(substring,ix)
        text = text[0:ix]+text[ix+len(substring):] #this slices out text without first occurence of the substring

    return text


print(remove_substring('Mississippi','iss'))
print(remove_substring('bicycle','cyc'))
print(remove_substring('tututututututu','tu'))
print(remove_substring('bicycle','eggs'))
