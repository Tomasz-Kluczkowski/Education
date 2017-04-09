def is_merge(s, part1, part2):
    """Returns True if parts can be merged to create string s maintaining the letter order"""
    # starting indexes for search of letters
    ip_1 = 0
    ip_2 = 0
    ix_s = 0
    while ix_s < len(s):
        if ip_1 < len(part1):
            print("letter from part1: {0}".format(part1[ip_1]))
        if ip_2 < len(part2):
            print("letter from part2: {0}".format(part2[ip_2]))
        print("looking for letter from s: {0}".format(s[ix_s]))
        if ip_1 < len(part1) and part1[ip_1] == s[ix_s]:
            ip_1 += 1
            ix_s += 1
        elif ip_2 < len(part2) and part2[ip_2] == s[ix_s]:
            ip_2 += 1
            ix_s += 1
        else:
            return False
    # check if both parts have been exhausted and only then return True
    if ip_1 == len(part1) and ip_2 == len(part2):
        return True
    else:
        return False

print(is_merge("Bananas from Bahamas", "Bahms", "ananas from Baa"))
print(is_merge("Bananas", "Baa", "nnas"))
