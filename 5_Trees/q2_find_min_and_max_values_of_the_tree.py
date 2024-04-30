"""
Write methods to find the minimum and maximum values of a tree
Given a basic BST structure (included), write two methods: one, called find_maximum(), to find the maximum value
of the tree and another one, called find_minimum(), to find the minimum value of the tree.
The methods should not accept parameters and return the nodes containing the maximum and minimum
values of the tree respectively. The basic definition for the methods are already included.

"""


class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'


class Tree():
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        """
        Inserts a new value in the BST

        Parameters:
        - 'data': Value or data to insert

        Returns: None
        """
        # Using a couple of pointers to traverse the tree, following BST rules
        # and find the parent of the node to be inserted
        current_node = self._root_node
        parent_node = None
        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        # After the loop, parent_node variable is parent node or None (if Tree is empty)
        new_node = Node(data, parent_node=parent_node)
        if parent_node is None:
            if self._root_node is None:
                # If tree is empty, -> make the new node - the root node
                self._root_node = new_node
            else:
                # If tree is not empty and parent_node is None, most likely an error.
                raise (ValueError)
        elif new_node.data < parent_node.data:
            # If value of new node is smaller than parent's, add new node to its left
            parent_node._left_child = new_node
        else:
            # If value of new node is bigger than parent's, add new node to its right
            parent_node._right_child = new_node

    def _find(self, data):
        """
        Find the node containing the data.

        Parameters:
        - 'data': The data to be found

        Returns:
        - The node that contains such data or None if data is not found
        """
        current = self._root_node
        while current:
            if current.data == data:
                return current
            elif current.data > data:
                current = current._left_child
            else:
                current = current._right_child
        return None

    def find_minimum(self):
        """
        Returns the minimum value of the tree
        """
        current_node = self._root_node

        # Traverse left children until the most-left leaf node is reached
        while current_node and current_node._left_child:
            current_node = current_node._left_child

        return current_node

    def find_maximum(self):
        """
        Returns the maximum value of the tree
        """
        current_node = self._root_node

        # Traverse right children until the most-right leaf node is reached
        while current_node and current_node._right_child:
            current_node = current_node._right_child

        return current_node


tree = Tree()
tree.insert(50)
tree.insert(20)
tree.insert(70)
tree.insert(90)
tree.insert(10)
tree.insert(40)
tree.insert(30)
tree.insert(35)
minimum = tree.find_minimum()
maximum = tree.find_maximum()
print(minimum, maximum) # 10<><># 90<><>#
