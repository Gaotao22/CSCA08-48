## Create a BSTNode for non-empty nodes in the BST.
## If a node is empty, use a BSTEmptyNode which has
## all the same methods and functions



class BSTNode():
    '''A node in a binary search tree.'''
    
    def __init__(self, data):
        '''(BSTNode, object) -> NoneType
        Initialize a new node to contain data, and empty 
        left and right children.
        '''
        self.data = data
        # make sure user doesn't jeopardize the ordering
        self.right = BSTEmptyNode()
        self.left = BSTEmptyNode()

    def __str__(self):
        '''(BSTNode) -> str
        Return a str representation of the tree rooted
        at self.
        '''
        
        return self._str_helper('\t', 0)
    
    def _str_helper(self, indent, level):
        '''(BSTNode, str, int) -> str
        Return a str representation of the tree with subtrees indented at by indent.
        '''
        # first recursively str right subtree (indent 1 more)
        return_str = self.right._str_helper(indent, level+1)
        # convert the root to a str
        return_str += indent*level + str(self.data) + "\n"
        # recursively str left subtree (indent 1 more)
        return_str += self.left._str_helper(indent, level+1)

        return return_str
    
    
    def insert(self, value):
        '''(BSTNode, object) -> BSTNode
        Return the root of the updated tree with value
        inserted.
        '''
        # if the value is smaller than the root
        # go left
        if (value < self.data):
            self.left = self.left.insert(value)
        else:
            # go down the right subtree
            self.right = self.right.insert(value)
        
        return self

    def search(self, value):
        '''(BSTNode, object) -> bool
        Return True if the value is in the tree and
        False otherwise.
        '''
        # if value is the current, fount it
        if (value == self.data):
            return True
        # otherwise, look in right or left subtree
        elif (value < self.data):
            # look in the left side
            return self.left.search(value)
        else:
            return self.right.search(value)

    def delete(self, value):
        '''(BSTNode, object) -> BSTNode
        Return the updated tree rooted at self, with value removed.
        '''
        if (self.data == value):
            # found it!! delete it
            # if left child is empty    
            # make the node its right child
            if self.left.is_empty():    
                self = self.right
                # if right child is empty
                # make he node its left child
            elif self.right.is_empty():
                self = self.left
                # if both children non-empty
                # find successor and replace the node with it
                # delete the successor
            else:
                self.data = self.right._find_smallest()
                self.right = self.right.delete(self.data)
        elif (value < self.data):
            self.left = self.left.delete(value)
        else:
            self.right = self.right.delete(value)

        return self

    def _find_smallest(self):
        '''(BSTNode) -> object
        Return the smallest, or leftmost nodes value
        in the subtree rooted at self.
        '''
        if self.left.is_empty():
            return self.data
        else:
            return self.left._find_smallest()
        
    def is_empty(self):
        '''(BSTNode) -> bool
        Return False since it is a non-empty node.
        '''
        return False
        
class BSTEmptyNode(BSTNode):
    '''A special case of the BSTNode - the empty node.
    '''
    
    def __init__(self):
        '''(BSTEmptyNode) -> NoneType
        Make our init function do nothing.
        '''
        pass
    
    def __str__(self):
        '''(BSTEmptyNode) -> str
        Return a blank line for the empty node representation.
        '''
        return '\n'
    
    def _str_helper(self, indent, level):
        '''(BSTEmptyNode, str, int) -> str
        Ignore the level and indent and return a new line
        str.'''
        return '\n'
    
    def insert(self, value):
        '''(BSTEmptyNode, object) -> BSTNode
        Create a BSTNode for the given value and 
        return it as the new root
        
        '''
        return BSTNode(value)
        
    def search(self, value):
        '''(BSTEmptyNode, object) -> bool
        Return False, since the value is not in an
        empty node.
        '''
        return False
    
    def delete(self, value):
        '''(BSTEmptyNode, object) -> BSTEmptyNode
        Return the empty node as value must not
        be in the tree.
        '''
        return self
    
    def is_empty(self):
        '''(BSTEmptyNode) -> bool
        Return True since it is an empty node.
        '''
        return True
    
class BSTree():
    '''A binary search tree class using BSTNodes.'''
    
    def __init__(self, init_values = []):
        '''(BSTree [, list of objects]) -> NoneType
        Initialize a binary search tree to the optionally 
        passed list of values.
        '''
        self.root = BSTEmptyNode()
        for value in init_values:
            self.insert(value)
    
    def __str__(self):
        '''(BSTree) -> str
        Return a string representation of the tree.
        '''
        return self.root.__str__()
    
    
    def insert(self, value):
        '''(BSTree, object) -> NoneType
        Insert the given value into the binary search tree.
        REQ: value is not already in the tree.
        '''
        self.root = self.root.insert(value)
    
    def search(self, value):
        '''(BSTree, object) -> bool
        Return True if the value is in the tree and 
        False otherwise.
        '''
        return self.root.search(value)

    def delete(self, value):
        '''(BSTree, object) -> NoneType
        Remove the given value from the tree if 
        it exists.
        '''
        self.root = self.root.delete(value)
            
if __name__ == '__main__':
    my_tree = BSTree([2, 5, 7, 10, 11, 15, 20])
    print(my_tree)
    #my_tree.delete(20)
    #print(my_tree, '*'*15)
    
    #my_tree.insert(8)
    #my_tree.insert(6)
    #print(my_tree, '*'*15)
    #my_tree.delete(5)
    #print(my_tree)    