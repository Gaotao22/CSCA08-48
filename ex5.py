def edit_distance(s1, s2):
    total = 0
    if len(s1) == len(s2) == 1:
        if s1 != s2:
            total += 1
        return total
    else:
        if s1[0] != s2[0]:
            total += 1
        return total + edit_distance(s1[1:], s2[1:])


def subsequence_helper(s1, s2):
    total = 0
    if len(s2) < len(s1) or s1 == '':
        pass
    elif len(s1) == 1 == len(s2) == 1:
        if s1 == s2:
            return 1
        else:
            return 0
    elif len(s1) == 1:
        if s1 == s2[-1]:
            return 1
        else:
            return subsequence_helper(s1, s2[:-1])
    else:
        if s1[-1] == s2[-1]:
            add = subsequence_helper(s1[:-1], s2[:-1])
            total = 1 + add
        else:
            total = subsequence_helper(s1, s2[:-1])
    return total


def subsequence(s1, s2):
    return subsequence_helper(s1, s2) == len(s1)


def gcd(a, b):
    if abs(a) >= abs(b) and b != 0:
        a = a % b
    elif abs(b) > abs(a) and a != 0:
        b = b % a
    if a == 0:
        if b < 0:
            return b
        else:
            return abs(b)
    elif b == 0:
        if a > 0:
            return a
        else:
            return abs(a)
    else:
        return_v = gcd(a, b)
        return return_v
