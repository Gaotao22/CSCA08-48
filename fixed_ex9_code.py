class Heap(object):
    '''A class representing a heap.'''
    
    def __init__(self, insert_list=[]):
        '''(Heap [,list]) -> NoneType
        Create a new Heap containing the elements in insert_list.
        '''

        self._heap = []
        for element in insert_list:
            self.insert(element)

    def is_empty(self):
        '''(Heap) -> bool
        Return True iff there are no nodes in this Heap.
        '''

        self._heap = []

    def insert(self, insert_value):
        '''(Heap, object) -> NoneType
        Insert insert_value into this Heap.
        REQ: insert_value is not already in this Heap.
        '''

        self._heap.append(insert_value)
        self._bubble_up(len(self._heap) - 1)

    def _bubble_up(self, c_index):
        '''(Heap) -> NoneType
        
        Re-arrange the values in this Heap to maintain the heap
        property after a new element has been inserted into the
        heap. The offending child node is located at c_index.
        '''

        p_index = (c_index - 1) // 2
        #Base Case: We're at the beginning of the list, do nothing
        if c_index > 0:
            if self._heap[c_index] > self._heap[p_index]:
                #swap the parent and child
                self._swap(c_index, p_index)
                #RD: bubble up again from our new position
                self._bubble_up(c_index)
                

    def _swap(self, i, j):
        '''(Heap, int, int) -> NoneType
        Swap the values at indices i and j.
        '''

        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def remove_top(self):
        '''(Heap) -> object
        Remove and return the largest element in this Heap.
        RAISES: HeapEmptyException if this Heap is empty.
        '''

        if self._heap == 0:
            raise HeapEmptyException("Attempt to remove top of empty heap")
        else:
            #save the top element
            ret = self._heap[0]
            #remove the last element from the heap, and 
            #replace the head's value with it
            last = self._heap.pop()
            if len(self._heap) > 0:
                self._heap[0] = last
                self._bubble_down(0)
            return ret

    def _bubble_down(self, p_index):
        '''(Heap) -> NoneType

        Re-arrange the values in this Heap to maintain the heap
        property after the top element of the heap has been removed.
        The parent node which potentially violates the heap property
        is located at p_index.
        '''

        lt_index = (p_index * 2) + 1
        rt_index = (p_index * 2) + 2
        #Base Case: If we don't violate, then do nothing
        if self._violates(p_index):
            #one of our children violates the heap property
            #if we only have a left child, it must be that one
            if rt_index >= len(self._heap):
                self._swap(p_index, lt_index)
                p_index = lt_index
               
            #if we have two children, we need to swap with the larger child
            elif self._heap[lt_index] > self._heap[rt_index]:
                self._swap(p_index, lt_index)
                p_index = lt_index
            else:
                self._swap(p_index, rt_index)
                p_index = rt_index
        #RD: Bubble down from our new position
        self._bubble_down(p_index)

    def _str_helper(self, index = 0, depth = 0):
        '''(Heap [, int, int]) -> str
        Return a str representation of the heap.
        '''
        if index > len(self._heap) - 1:
            return ''
        
        return_str = self._str_helper(2*index+2, depth+1)
        return_str += '\t'*depth + str(self._heap[index]) + '\n'
        return_str += self._str_helper(2*index+1, depth+1)
        return return_str    
    
    def __str__(self):
        '''(Heap) -> str
        A str representation of the heap.
        '''
        return str(self._heap) + '\n' + self._str_helper()        
        
if __name__ == '__main__':
    my_heap = Heap([5, 1, 10, 2, 4, 8, 9, 3, 0])
    print(my_heap)
    my_list = []
    my_heap.insert(3)