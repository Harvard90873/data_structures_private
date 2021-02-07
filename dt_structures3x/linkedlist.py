# Import =====================================================================================
from .binarytree import Node as inheritance                                                 #||
try:                                                                                       #||
    from algorithms3x import bubble_sort                                                   #||
except ImportError:                                                                        #||
    raise ImportError("Please install the package: pip install python-algorithms-3x")      #||
# ============================================================================================

class Item(inheritance):
    """
    An item for linked lists\n
    Note that it is only for linked lists. In the case of hash tables, please use the 'Node' class
    """
    def __init__(self, val=None, pointer=None):
        self.val = val
        self.pointer = pointer
    def getNextNode(self):
        return self.pointer
    def appendChild(self, *args):
        """
        Append child to the item, if there is already one, append to the end of the linked list
        """
        for child in args:
            tmp = self
            if self.pointer == None:
                self.pointer = child
                while tmp.pointer != None:
                    tmp = tmp.pointer
            else:
                while tmp.pointer != None:
                    tmp = tmp.pointer
                tmp.pointer = child