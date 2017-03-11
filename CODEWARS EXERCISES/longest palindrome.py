from unit_testing import test

def longest_palindrome(s):
    """ Find longest possible substring that is a palindrome """
    """ have to check from first index to last and reversing after increasing the index """
    """ then increase the first index and check till end again """
    ix1 = 0
    ix2 = 1
    substring = ""
    while True:

        sub = s[ix1:ix2]
        if sub == sub[::-1]:
            if len(sub) > len(substring):
                substring = sub
        if ix2 < (len(s)):
            ix2 += 1
            continue
        else:
            if ix1 < (len(s)-2):
                ix1 += 1
                ix2 = ix1 + 1
                continue

        return len(substring)

test(longest_palindrome("baablkj12345432133d"), 9)












