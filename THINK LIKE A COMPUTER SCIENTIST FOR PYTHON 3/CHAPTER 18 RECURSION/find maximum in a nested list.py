from unit_testing import test


def r_max(nxs):
    """Find the maximum in a recursive structure of lists within other lists.
    Precondition: no lists or sublists are empty."""
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e

        if first_time or val > largest:
            largest = val
            first_time = False

    return largest

test(r_max([2,9,[1,13],8,6]), 13)