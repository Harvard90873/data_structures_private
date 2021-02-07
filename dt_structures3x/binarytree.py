class Node:
    """
    Item in a binary tree
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"Node id: <{id(self)}> | value: {self.val}"
    def get_children(self):
        """
        Gets children from left to right, returns a set
        """
        return (self.left, self.right)
    