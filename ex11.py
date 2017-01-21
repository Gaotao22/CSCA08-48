class ContainerFullException(Exception):
    '''
    '''

class ContainerEmptyException(Exception):
    '''
    '''

class Stack():
    def __init__(self):
        self._list = []
    
    def __str__(self):
        return str(self._list)

    def put(self, e):
        self._list.append(e)

    def get(self):
        if self.is_empty():
            raise ContainerEmptyException
        return self._list.pop(-1)

    def peek(self):
        if self.is_empty():
            raise ContainerEmptyException
        return self._list[-1]

    def is_empty(self):
        return self._list == []

class Queue():
    def __init__(self):
        self._list = []

    def put(self, e):
        self._list.append(e)

    def get(self):
        if self.is_empty():
            raise ContainerEmptyException        
        return self._list.pop(0)

    def peek(self):
        if self.is_empty():
            raise ContainerEmptyException        
        return self._list[0]

    def is_empty(self):
        return self._list == []

class Bucket():
    def __init__(self):
        self._list = []

    def put(self, e):
        if len(self._list) == 1:
            raise ContainerFullException
        self._list.append(e)

    def get(self):
        if self.is_empty():
            raise ContainerEmptyException        
        return self._list.pop(0)

    def peek(self):
        if self.is_empty():
            raise ContainerEmptyException        
        return self._list[0]

    def is_empty(self):
        return self._list == []

def banana_game(s1, s2, c):
    print(s1, s2, c)
    # see whether s1 is empty
    if s1 != '':
        # if s1 is not empty but s2 is empty, return false directly
        if s2 == '':
            return False
        # compare the first letters of s1 and s2
        
            
        # if the first letters are not identical
        
            # get the first letter in the container
        last_letter_c = ''
        if not c.is_empty():
            last_letter_c = c.peek()
        print(last_letter_c, s2[0])
        # compare the two letters
        if last_letter_c == s2[0]:
            # if they match, truncate both s2 and container
            c.get()
            s2 = s2[1:]
        # if they don't match
        else:
            if s1[0] == s2[0]:
            # shorten both of them if their first letters are identical
                s1 = s1[1:]
                s2 = s2[1:]
            else:
                # if the container is not full
                try:
                    # add the first letter of s1 to container
                    c.put(s1[0])
                    # shorten s1
                    s1 = s1[1:]
                # if the container is full
                except ContainerFullException:
                    # return false since no operation is available
                    return False  
    # when s1 is completely unloaded, define the base case
    else:
        # get out the elements in the container and compare the letters
        result = ''
        while not c.is_empty():
            result = result + c.get()
        # test if the letters from the container is equal to s2
        return result == s2
    # recurse
    return banana_game(s1, s2, c)

if __name__ == '__main__':
    c = Stack()
    d = Queue()
    e = Bucket()
    print(banana_game('BANANA', 'NABANA', d))
