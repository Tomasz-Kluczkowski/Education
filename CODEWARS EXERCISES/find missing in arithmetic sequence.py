import time
t0 = time.clock()
def find_missing(sequence):
    """Return missing item in the arithmetic sequence"""
    dx = (sequence[-1] - sequence[0]) / len(sequence)
    for i in range(len(sequence) + 1):
        elem = sequence[0] + i * dx
        if elem not in sequence:
            return elem
t1 = time.clock()

print(find_missing([1, 2, 3, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]))
print("{0:4f}".format(float(t1 - t0)))