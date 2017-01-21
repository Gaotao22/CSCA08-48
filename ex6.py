class DLLNode(object):
    '''This class builds the node for doubly linked list and sorted list. It
       can connect with its previous and the next node but initiate with none
       in its previous and next nodes.
     '''

    def __init__(self, data, prev_node=None, next_node=None):
        '''(DLLNode, obj, [DLLNode, DLLNode]) -> Nonetype
        '''
        # initiate the DLLNode with the input data, previous and next nodes
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node


class DLList(object):
    '''This doubly linked list was built up with both head and tail. The nodes
       within can be traced forward and backward.
    '''

    def __init__(self):
        '''(DLList) -> Nonetype
           Initiate the doubly linked list
        '''
        self.head = None
        self.tail = None

    def add_to_head(self, new_obj):
        '''(DLList, obj) -> Nonetype
           add the obj to its head
        '''
        # Classify the new_obj
        new_node = DLLNode(new_obj)
        # When the self.head is Nonetype, add the node to the head
        if self.head is None:
            self.head = new_node
        # Add new_node before existant self.head
        else:
            tmp = self.head
            tmp.prev_node = new_node
            new_node.next_node = tmp
            self.head = new_node
        # Equalize self.head and self.tail if there is only one element in the
        # doubly linked list
        if new_node.next_node is None:
            self.tail = new_node

    def add_to_tail(self, new_obj):
        '''(DLList, obj)->Nonetype
        Add the obj to the tail of the linked list
        '''
        # classify the input obj
        new_node = DLLNode(new_obj)
        # add the node to the tail directly if the tail is None
        if self.tail is None:
            self.tail = new_node
        # trace up to the correct position, adding the node to the tail
        else:
            tmp = self.tail
            tmp.next_node = new_node
            new_node.prev_node = tmp
            self.tail = new_node
        # the tail should equal to the head when the head is None
        if new_node.prev_node is None:
            self.head = new_node

    def search(self, data):
        '''(DLList, obj) -> int
        Return the position of the data for which it was looked. When it does
        not exist in the linked list, return -1
        '''
        # define the possible index of the object
        count = 0
        # create a tmporary element that iterate each element
        tmp = self.head
        # iterate when the tmporary element is not empty
        while tmp is not None:
            # compare the obj and the data of the element
            if tmp.data == data:
                # return the position of the element if it fit
                return count
            # count accumulate to fit the incremental position
            count += 1
            # iterate to the next node
            tmp = tmp.next_node
        # return -1 when the obj is not in the linked list
        return -1

    def remove_head(self):
        '''(DLList) -> int
        Remove the head from the linked list.
        '''
        tmp = self.head
        self.head = self.head.next_node
        self.head.prev_node = None
        if self.head is None:
            self.tail = None
        return tmp

    def remove_tail(self):
        '''(DLList) -> int
        Remove the tail of the linked list.
        '''
        tmp = self.tail
        self.tail = self.tail.prev_node
        self.tail.next_node = None
        if self.tail is None:
            self.head = None
        return tmp


class SortedList(object):
    '''This sorted list sort out the input elements with their data. Each
    element has prev_node and next_node to connect its previous and next value
    '''

    def __init__(self):
        '''(SortedList) -> Nonetype
        Initiate the sorted list, setting both self.head and self.tail None.
        '''
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, new_obj):
        '''(SortedList, obj) -> Nonetype
        Add each node with the ojbect as its data in to the sorted list. The
        node will be added to right position in accordance with its value.
        '''
        new_node = DLLNode(new_obj)
        self.length += 1
        if self.head is None:
            self.head = self.tail = new_node
        else:
            node = self.head
            while node is not None:
                if node.data >= new_obj:
                    if node.prev_node is not None:
                        tmp = node.prev_node
                        tmp.next_node = new_node
                        new_node.prev_node = tmp
                    else:
                        self.head = new_node
                    new_node.next_node = node
                    node.prev_node = new_node
                    return
                node = node.next_node
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

    def remove(self, new_obj):
        '''(SortedList, obj) -> Nonetype
        Remove the node with the specified element from the sorted list.
        '''
        node = self.head
        while node is not None:
            if node.data == new_obj:
                self.length -= 1
                if node.prev_node is None and node.next_node is None:
                    self.__init__()
                elif node == self.head:
                    self.head = node.next_node
                    self.head.prev_node = None
                elif node == self.tail:
                    self.tail = node.prev_node
                    self.tail.next_node = None
                else:
                    tmp1 = node.prev_node
                    tmp2 = node.next_node
                    tmp1.next_node = tmp2
                    tmp2.prev_node = tmp1
                return
            node = node.next_node

    def middle(self):
        '''(Sortedlist) -> Nonetype
        Find the element in the middle. If there are two nodes in the middle,
        return the element of the one closer to the head.
        '''
        if self.length == 0:
            return
        num = self.length // 2 + self.length % 2
        node = self.head
        for index in range(1, num):
            node = node.next_node
        return node.data
