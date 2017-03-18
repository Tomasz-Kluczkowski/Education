from unit_testing import test

def tribonacci(signature,n):
    trib_dict = {number:signature[number-1] for number in range(1, 4)}
    if n == 0:
        return []
    for pos in range(4, n+1):
        trib_dict[pos] = trib_dict[pos-3] + trib_dict[pos-2] + trib_dict[pos-1]
    return [trib_dict[key] for key in range(1, n+1)]

test(tribonacci([1,1,1],10),[1,1,1,3,5,9,17,31,57,105])