def banana_game(s1, s2, c):
    if s1 != '':
        if s2 == '':
            return False
        if s1[0] == s2[0]:
            s1 = s1 [1 : ]
            s2 = s2 [1 : ]
        else:
            last_letter_c = ''
            if not c.is_empty():
                last_letter_c = c.peek()
            if last_letter_c == s2[0]:
                c.get()
                s2 = s2 [1 : ]
            else:
                try:
                    c.put(s1[0])
                    s1 = s1[1:]
                except ContainerFullException:
                    return False
    else:
        result = ''       
        while not c.is_empty():
            result = result + c.get()
        return result == s2
    return banana_game(s1, s2, c)
        
                