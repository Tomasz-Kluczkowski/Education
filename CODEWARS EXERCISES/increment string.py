def increment_string(strng):
    import string
    suffix = ""
    prefix = ""
    if len(strng) == 0:
        return "1"
    elif strng[-1] not in string.digits:
        return strng + "1"
    else:
        for ix in range((len(strng)-1), -1,-1):
            if strng[ix] in string.digits:
                suffix += strng[ix]
            else:
                prefix = strng[0:ix+1]
                break
    suffix_num = int(suffix[::-1])
    modifier = len(str(suffix_num + 1)) - len(str(suffix_num))
    return prefix + "0" * (len(suffix) - len(str(suffix_num)) - modifier) + str(suffix_num + 1)

print(increment_string("foobar099"))