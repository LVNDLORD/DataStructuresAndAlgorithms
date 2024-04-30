"""
Write a method that detach a node from the tree
Given a basic BST structure (included), add a _detach_node() method to it, to search for values in the tree.
he basic definition of the method is already included. The method accepts the node to be deleted as parameter and
returns nothing.

The method should check on parent and possible children to change the connections and be sure that the tree remains
functional after safely detaching the node from the tree. If the node to detach has two children,
the method should raise a ValueError (it is not possible to just detach a node with two children from a BST).
The method should also take into account when the node to detach is the root node.

Notice that the Node object, when printed, prints some odd code.
This is done on purpose to help checking on the exercises.
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

    def _detach_node(self, node):
        """
        Detach a node from the tree. Node to be detached has one child at most.
        An error will be raised otherwise.
        """
        # Case 1: Node has no children (leaf node)
        if node._left_child is None and node._right_child is None:
            if node._parent is None:
                # If the node is the root node, set the root to None
                self._root_node = None
            elif node._parent._left_child == node:
                # If the node is a left child, remove the reference from its parent's left child
                node._parent._left_child = None
            else:
                # If the node is a right child, remove the reference from its parent's right child
                node._parent._right_child = None

        # Case 2: Node has one child
        elif node._left_child is None:
            # If the node has only a right child, connect the right child to its parent
            if node._parent is None:
                # If the node is the root node, set the right child as the new root
                self._root_node = node._right_child
            elif node._parent._left_child == node:
                # If the node is a left child, connect its parent to its right child
                node._parent._left_child = node._right_child
            else:
                # If the node is a right child, connect its parent to its right child
                node._parent._right_child = node._right_child
            if node._right_child:
                # Update the parent reference of the right child
                node._right_child._parent = node._parent

        elif node._right_child is None:
            # If the node has only a left child, connect the left child to its parent
            if node._parent is None:
                # If the node is the root node, set the left child as the new root
                self._root_node = node._left_child
            elif node._parent._left_child == node:
                # If the node is a left child, connect its parent to its left child
                node._parent._left_child = node._left_child
            else:
                # If the node is a right child, connect its parent to its left child
                node._parent._right_child = node._left_child
            if node._left_child:
                # Update the parent reference of the left child
                node._left_child._parent = node._parent

        # Case 3: Node has two children
        else:
            raise ValueError("Cannot detach a node with two children from a BST")


tree = Tree()
tree.insert(50)
tree.insert(20)
tree.insert(70)
tree.insert(90)
tree.insert(10)
tree.insert(40)
tree.insert(30)
tree.insert(35)
node = tree._find(30)
tree._detach_node(node)
print(tree._find(tree._root_node.data))  # 50<20<10<><>#><40<35<><>#><>#>#><70<><90<><>#>#>#
