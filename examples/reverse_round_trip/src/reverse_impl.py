def reverse_correct(lst):
    return lst[::-1]

def reverse_bug_1(lst):
    """The bug is that the reverse function is the identity function - it just returns the input"""
    return lst[:]

def reverse_bug_2(lst):
    """
    The bug is that we do one extra step. This works fine on odd-length lists but is not correct
    on lists with even length.
    """
    if lst == []:
      return []
    ret = lst[:]
    for i in range(int(len(ret)/2) + 1):
        ret[i], ret[len(ret)-i-1] = ret[len(ret)-i-1], ret[i]
    return ret

def reverse_bug_3(lst):
    """
    The bug is that the just rotates the list 1 step (puts the last element in 1st place)
    So this is correct for all lists up to length 2, but fails on length 3 or more.
    """
    if lst == []:
      return []
    return [lst[-1]] + lst[:-1]
