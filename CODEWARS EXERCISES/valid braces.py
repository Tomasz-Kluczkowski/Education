def validBraces(string):
    """Return True if string contains braces written in correct order"""
    # if number of braces is uneven return False straight away
    len_before_rem = len(string)
    if len(string) % 2 != 0:
       return False

    while len(string) > 0:
        for ix, char in enumerate(string):
            # if first character is any right side brace return False straight away
            if (ix == 0 and char in "]})"):
                return False
            elif char in "[{(":
                continue
            # here we start removing valid matching braces until all
            # are removed and the whole expression is confirmed valid
            elif char in "]})":
                if ((char == "]" and string[ix-1] == "[") or
                        (char == "}" and string[ix-1] == "{") or
                            (char == ")" and string[ix-1] == "(")):
                    len_before_rem = len(string)
                    string = string[0:ix-1]+string[ix+1:]

                    break
        if (len(string) > 0 and ix == (len_before_rem - 1)):
            return False
    return True




test_string = "{}()[]"
print(validBraces(test_string))


