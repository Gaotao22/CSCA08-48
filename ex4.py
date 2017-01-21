def rsum(received_list):
    total = 0
    if len(received_list) == 1:
        if isinstance(received_list[0], list):
            total += rsum(received_list)
        else:
            total += received_list[0]
    elif len(received_list) > 1:
        if  isinstance(received_list[0], list):
            total += rsum(received_list[0]) + rsum(received_list[1:])
        else:
            total += received_list[0] + rsum(received_list[1:])
    return total


def rmax(received_list):
    max_num = None
    if len(received_list) == 1:
        if isinstance(received_list[0], list):
            max_num = rmax(received_list[0])    
        else:
            max_num = received_list[0]    
    elif len(received_list) > 1:
        if isinstance(received_list[0] , list):
            first_num = rmax(received_list[0])
        elif received_list[0] == []:
            first_num = None
        else:
            first_num = received_list[0]
        max_num = rmax(received_list[1:])
        if first_num != None and max_num != None:
            if first_num > max_num:
                max_num = first_num
        if max_num == None:
            max_num = first_num
    return max_num


def two_smallest(received_list):
    if len(received_list) == 0:
        return (float('inf'), float('inf'))
    else:
        sec_num = two_smallest(received_list[1:])
        if not isinstance(received_list[0], list):
            first_num = received_list[0]
            if first_num <= sec_num[1]:
                return (sec_num[1], first_num)
            elif first_num > sec_num[1] and first_num < sec_num[0]:
                return (first_num, sec_num[1])
            else:
                return sec_num
        else:
            first_num = two_smallest(received_list[0])
            return two_smallest([first_num[0], sec_num[0], 
                               first_num[1], sec_num[1]])

      
def second_smallest(received_list):
    sec_small = two_smallest(received_list)[0]
    if sec_small != float('inf'):
        return sec_small
    
    
def max_min(received_list):
    if received_list == []:
        return (float('inf'), -float('inf'))
    elif len(received_list) == 1 and isinstance(received_list[0], int):
        return (received_list[0], received_list[0])
    elif len(received_list) == 1 and isinstance(received_list[0], float):
            return ()
    else:
        if isinstance(received_list[0], int):
            first_num = received_list[0]
            sec_num = max_min(received_list[1:])
            if sec_num == ():
                return (first_num, first_num)
            elif first_num <= sec_num[0]:
                return (first_num, sec_num[1])
            elif first_num >= sec_num[1]:
                return (sec_num[0], first_num)
            else:
                return sec_num
        elif isinstance(received_list[0], list):
            first_num = max_min(received_list[0])
            sec_num = max_min(received_list[1:])
            if sec_num == ():
                return max_min([first_num[0], first_num[1]])
            elif first_num == ():
                return max_min([sec_num[0], sec_num[1]])
            else:
                return max_min([first_num[0], first_num[1], 
                                sec_num[0], sec_num[1]])
        else:
            return max_min(received_list[1:])

def sum_max_min(received_list):
    if max_min(received_list) == (float('inf'), -float('inf')):
        return None
    elif max_min(received_list) == ():
        return None
    else:
        return max_min(received_list)[0] + max_min(received_list)[1]