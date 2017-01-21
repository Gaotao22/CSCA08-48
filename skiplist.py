import random
# pre-define the magic number as constant
# the list start from one which is also the step for iteration
start = step = 1
# the firstelement of a string is starting from 0
first_element = first_step = 0
# the fixed probability to randomize num of levels
fixed_probability = 0.5


class Node():
    '''The regular node that takes a data and connect with the next node in
    linked list.
    '''

    def __init__(self, data, next_node=None):
        '''(Node, obj, Node) -> Nonetype
        It initiates this class by adding its data and the node connected next.
        The next node is defualt as None.
        '''
        self.data = data
        self.next_node = next_node

    def __str__(self):
        '''(Node) -> str
        It returns the data of the Node unless it is a head node.
        '''
        # see first whether the data is negative inf. If so, return the str
        # Head
        if self.data == -float('inf'):
            return 'Head'
        # or return the data
        return str(self.data)


class Ref_Node(Node):
    '''The Node that can reference to the node with the same value in the lower
    layer. As well, it connects to its next node like a regular Node because it
    is inherited from the Node.
    '''

    def __init__(self, data, next_node=None, refer_node=None):
        '''(Ref_Node, obj, [Ref_Node, Node]) -> Nonetype
        This intialize the Ref_Node and leave the data and next_node to the
        factors it has inherited from Node. The refer_node is the new unique
        function of this class.
        '''
        # Implement with its parent class Node
        Node.__init__(self, data, next_node)
        # add value to its refer_Node function
        self.refer_node = refer_node

    def __str__(self):
        '''(Ref_Node) -> str
        Return the data in the Ref_Node.
        '''
        return str(self.data)


class Start_Node(Ref_Node):
    '''The node at the start with a negative infinite sign. It inherits from
    the Ref_Node
    '''
    def __init__(self):
        '''(Start_Node) -> Nonetype
        Initialize the Start_Node with implementing Ref_Node
        '''
        Ref_Node.__init__(self, -float('inf'))

    def __str__(str):
        '''(Start_Node) -> str
        Return the str Head
        '''
        return 'Head'


class End_Node(Ref_Node):
    '''The node at the end only with an infinite sign, inheriting from Node.
    '''
    def __init__(self):
        '''(End_Node) -> Nonetype
        Intialize the End_Node by implementing the functions in Node. Plus the
        data parameter is specified to be positive infinite.
        '''
        Ref_Node.__init__(self, float('inf'))

    def __str__(self):
        '''(End_Node) -> str
        Return str Tail.
        '''
        return 'Tail'


class SkipList():
    '''This is a data structure that ease the search of an element in the
    middle. It may have multiple levels with some elements from the linked list
    in the first level being skiped. This can quicken the search machanism when
    an element far after the head required to be sought.
    '''
    def __init__(self, probability=fixed_probability):
        '''(self, [int]) -> Nonetype
        Intiate the skip list with the fixed probability.
        '''
        # set the head of the first level to be an empty Start_Node
        self.head = Start_Node()
        # set the tail of the first level to be an empty End_Node
        self.tail = End_Node()
        # connect self.head and self.tail since they don't have element in
        # between
        self.head.next_node = self.tail
        # The height of the Skip list
        self.level = start
        # the head of the top level is self.head because it just has one level
        self.top_head = self.head
        # the tail of the top level is self.tail because it just has one level
        self.top_tail = self.tail
        # the probability is always the fixed_probability
        self.probability = probability
        self.length = first_element

    def __str__(self):
        '''(SkipList) -> str
        Return the content of the skiplist in the required form
        '''
        # define a return_value and initiate it to be 0
        return_value = ''
        # start to add the element from the self.top_head
        head_node = self.top_head
        # iterate through the first column that contains only Start_Node
        while head_node is not None:
            # set the first node to be the head node and iterate in each row
            node = head_node
            return_value += 'Head->'
            while node.next_node is not None:
                node = node.next_node
                # add the element before the tail
                if node.data != float('inf'):
                    return_value = return_value + str(node.data) + '->'
                else:
                    # add tail when it reaches the last one
                    return_value += 'Tail'
            # change line when it is not in the last row
            if head_node.refer_node is not None:
                return_value += '\n'
            # go to the next row
            head_node = head_node.refer_node
        # return the value it needs to print
        return return_value

    def type_converter(self, node):
        '''(SkipList, Node/Ref_Node) -> obj
        It converts the type of the data when the data of different types need
        to be compared.
        '''
        # test whether the data is str
        if type(node.data) == str:
            # if so see its length, if its length is one, convert itself to the
            # type required
            if len(node.data) == start:
                    # take the order of the alphabet
                if node.data.isalpha():
                    return ord(node.data)
                else:
                    return float(node.data)
            else:
                # then see if the data with long length is convertible to
                # float for the comparison. If not, take the first character of
                # then convert it to float
                contain_nondecimal = False
                for element in node.data:
                    decimal_point = first_step
                    if not element.isnumeric():
                        if element == '.':
                            decimal_point += 1
                        else:
                            contain_nondecimal = True
                    if decimal_point > start:
                        contain_nondecimal = True
                if contain_nondecimal:
                    if node.data[first_element].isalpha():
                        return ord(node.data[first_element])
                    else:
                        return float(node.data[first_element])
                else:
                    return float(node.data)
        else:
            # or remain unchanged
            return node.data

    def insert_LinkedList(self, new_node, node=None):
        '''(SkipList, Node/Ref_Node, [Start_Node]) -> Nonetype
        Add the element to its right position based on its magnitude
        '''
        if node is None:
            node = self.head
        while node.next_node is not None:
            if type(new_node.data) == type(node.next_node.data):
                new_node_data = new_node.data
                next_node_data = node.next_node.data
            else:
                new_node_data = self.type_converter(new_node)
                next_node_data = self.type_converter(node.next_node)
            if next_node_data >= new_node_data:
                tmp = node.next_node
                node.next_node = new_node
                new_node.next_node = tmp
                return
            node = node.next_node

    def add_to_level(self, new_obj, level, bottom_node=None):
        new_node = Node(new_obj)
        if level == start:
            # add the new_node into the first level, the linked list
            self.insert_LinkedList(new_node)
        else:
            node_head = self.top_head
            for index in range(self.level - level):
                node_head = node_head.refer_node
            bottom_node = self.add_to_level(new_obj, level - 1)
            new_node = Ref_Node(new_obj)
            self.insert_LinkedList(new_node, node_head)
            new_node.refer_node = bottom_node
        return new_node

    def create_level(self, new_obj, level, bottom_node):
        '''
        When the level does not exist at first, create the levels and add the
        node into the level
        '''
        # define the top head
        new_head = Start_Node()
        new_head.refer_node = self.top_head
        self.top_head = new_head
        # define the new_node
        new_node = Ref_Node(new_obj)
        # add the head and the tail to it
        self.top_head.next_node = new_node
        # if the level is the first
        if level == start:
            # refer itself to the bottom_node
            new_node.refer_node = bottom_node
        else:
            # get the node which should be the bottom node in this case
            node = self.create_level(new_obj, level - step, bottom_node)
            # refer the new_node to the bottom node in this case
            new_node.refer_node = node
        new_tail = End_Node()
        new_node.next_node = new_tail
        new_tail.refer_node = self.top_tail
        self.top_tail = new_tail
        return new_node

    def level_generator(self):
        '''(SkipList) -> int
        Return the number of level it generated
        '''
        # initiate the number of level at 0
        level = 1
        # if the number generated by the random is smaller than the probability
        # the number of level will increase by each unit of step
        while random.uniform(0, 1) < self.probability:
            level += step
        # return the level
        return level

    def insert(self, new_obj):
        '''(SkipList, obj) -> Nonetype
        '''
        if self.level == 0:
            self.__init__()
        # generate the levels the number should be added
        level = self.level_generator()
        # just add the obj to the levels it's supposed to go to
        if level <= self.level:
            self.add_to_level(new_obj, level)
        else:
            # if its level surpassed the level of the skiplist, add to existing
            # level and create new ones
            new_node = self.add_to_level(new_obj, self.level)
            self.create_level(new_obj, (level - self.level), new_node)
            self.level = level
        self.length += 1

    def remove_level(self):
        while type(self.top_head.next_node) == End_Node:
            self.top_head = self.top_head.refer_node
            self.top_tail = self.top_tail.refer_node
            self.level -= step
            if self.top_head is None:
                return

    def remove(self, obj):
        head_node = self.top_head
        while head_node is not None:
            node = head_node
            while node is not None:
                if node.next_node is not None:
                    if node.next_node.data == obj:
                        target_node = node.next_node
                        while target_node.data == obj:
                            if type(target_node) == Node:
                                self.length -= 1
                            target_node = target_node.next_node
                        node.next_node = target_node
                node = node.next_node
            head_node = head_node.refer_node
            self.remove_level()

    def search(self, new_obj):
        '''(SkipList, obj) -> obj
        It can find whether the obj is contained in the skiplist. If it does,
        return the node. Or it should return None.
        '''
        head = self.top_head
        while head is not None:
            node = head
            while node is not None:
                if node.data == new_obj:
                    while type(node) == Ref_Node:
                        node = node.refer_node
                    return node
                node = node.next_node
            head = head.refer_node
        return
