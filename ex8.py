class BTNode(object):
    """A node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        """(BTNode, int, BTNode, BTNode) -> NoneType
        Initialize this node to store value and have children left and right,
        as well as depth 0.
        """
        self.value = value
        self.left = left
        self.right = right
        self.depth = 0  # the depth of this node in a tree

    def __str__(self):
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BTNode, str) -> str
        Return a "sideways" representation of the subtree rooted at this node,
        with right subtrees above parents above left subtrees and each node on
        its own line, preceded by as many TAB characters as the node's depth.
        """
        ret = ""

        if(self.right is not None):
            ret += self.right._str_helper(indentation + "\t") + "\n"
        ret += indentation + str(self.value) + "\n"
        if(self.left is not None):
            ret += self.left._str_helper(indentation + "\t") + "\n"
        return ret
    
    def set_depth(self, depth):
        self.depth = depth
        if self.left is not None:
            self.left.set_depth(depth + 1)
        if self.right is not None:
            self.right.set_depth(depth + 1)

    def read_depth(self):
        print(self.depth)
        if self.left is not None:
            self.left.read_depth()
        if self.right is not None:
            self.right.read_depth()

    def find_deepest(self, value_depth, number_go_through=[]):
        number_go_through.append(self.value)
        if self.left is not None:
            self.left.find_deepest(value_depth, number_go_through)
        if self.right is not None:
            self.right.find_deepest(value_depth, number_go_through)
        if self.left is None and self.right is None:
            value_depth.append((sum(number_go_through), self.depth))
        number_go_through.pop()
    
    def sum_to_deepest(self):
        self.set_depth(0)
        value_depth = []
        self.find_deepest(value_depth)
        print(value_depth)
        sums = []
        depth = []
        for element in value_depth:
            depth.append(element[1])
        max_depth = max(depth)
        for element in value_depth:
            if element[1] == max_depth:
                sums.append(element[0])
        return max(sums)
        
        

if(__name__ == "__main__"):
    # just a simple tree to practice on
    my_tree = BTNode(10, BTNode(3, BTNode(5), BTNode(2)),
                     BTNode(7, BTNode(4, BTNode(9)), BTNode(6)))
    print(my_tree)
    my_tree.set_depth(1)
    my_tree.read_depth()
    print(my_tree.sum_to_deepest())
