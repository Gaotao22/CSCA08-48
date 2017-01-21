def rsum(received_list):
    '''(list of int) -> (int)
    This function will take a list and return the sum of all elements.
    Exp:
    >>> rsum([1, 2, 3])
    6
    >>> rsum([0, 1, -3])
    -2
    '''
    if len(received_list) == 1:
        return received_list[0]
    else:
        return received_list[0] + rsum(received_list[1:])


def rmax(received_list):
    '''(list of int) -> int
    This function will take a list and return the maximum integer.
    Exp:
    >>> rmax([1, 2, 3])
    3
    >>> rmax([-1, 0, 1])
    1
    '''
    if len(received_list) == 1:
        return received_list[0]
    else:
        first_num = received_list[0]
        second_num = rmax(received_list[1:])
        if first_num > second_num:
            return first_num
        else:
            return second_num


def two_smallest(received_list):
    '''(list of int) -> tuple of int
    This function received the list and return the second minumum number and
    the minimum number in a tuple.
    Exp:
    >>> two_smallest([1, 3, 2, 5, 2])
    (2, 1)
    >>> two_smallest([1, 7, 3, 5, 9])
    (3, 1)
    '''
    # define the base case
    if len(received_list) == 2:
        # put the second smallest in the front of the smallest number
        # in a tuple
        if received_list[1] > received_list[0]:
            return (received_list[1], received_list[0])
        else:
            return (received_list[0], received_list[1])
    else:
        # recur the two_smallest(), take the original list without the first
        # item
        (sec_min_num, min_num) = two_smallest(received_list[1:])
        # compare the number returned from the last resursion with the first
        # number in the list
        if received_list[0] <= min_num:
            return (min_num, received_list[0])
        elif received_list[0] < sec_min_num and received_list[0] > min_num:
            return (received_list[0], min_num)
        else:
            return (sec_min_num, min_num)


def second_smallest(received_list):
    '''(list of int) -> (int)
    This function will take a list and return the second minimum integer.
    Exp:
    >>> second_smallest([1, 3, 2, 5, 2])
    2
    >>> second_smallest([1, 7, 3, 5, 9])
    3
    '''
    return two_smallest(received_list)[0]


def max_min(received_list):
    '''(list of int) -> tuple of int
    This function receives a list and return its maximum and minimum value
    in a tuple.
    Exp:
    >>> max_min([1, 5, 2, 9, 7])
    (9, 1)
    >>> max_min([1, 7, 5, 3, 2])
    (7, 1)
    '''
    # define 1 as base case
    if len(received_list) == 1:
        return (received_list[0], received_list[0])
    else:
        # receive the tuple from previous round of recursion
        (max_num, min_num) = max_min(received_list[1:])
        # compare the returned numbers with the first element in the received
        # list
        if received_list[0] > max_num:
            return (received_list[0], min_num)
        elif received_list[0] < min_num:
            return (max_num, received_list[0])
        else:
            return (max_num, min_num)


def sum_max_min(received_list):
    '''(list of int) -> int
    It receives the list of integers and return the the sum of the maximum
    and the minimum number
    Exp:
    >>> sum_max_min([1, 2, 3, 5, 9, 7])
    10
    >>> sum_max_min([2, -1, 3, 5, 9, 6])
    8
    '''
    # return the tuple tht saves the maximum and minimum of the list
    max_and_min = max_min(received_list)
    # add them up
    return max_and_min[0] + max_and_min[1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()