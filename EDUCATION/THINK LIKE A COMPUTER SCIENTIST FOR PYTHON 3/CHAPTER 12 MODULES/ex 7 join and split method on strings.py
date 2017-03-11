from unit_testing import test

def myreplace(old, new, s):
    """ Replace all occurences of old with new in s. """

    s = s.split()
    s = " ".join(s)

    return new.join(s.split(old))


test(myreplace(",", ";", "this, that, and some other thing"), "this; that; and some other thing")
test(myreplace(" ", "**", "Words will now      be  separated by stars."), "Words**will**now**be**separated**by**stars.")