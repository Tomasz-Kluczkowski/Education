def r_sum(nested_num_list):
    tot = 0
    for element in nested_num_list:
        if type(element) == type([]):
            tot += r_sum(element)
        else:
            tot += element
    return tot

test_list = [1,2,3,[1,2,3,[1,2,3,[12,3,4,[12,3,4]]]]]

print(r_sum(test_list))