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