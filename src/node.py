class Node:
    """
    A class used to represent a Node in a doubly linked list.

    Attributes
    ----------
    count : int
        The count associated with the node (default is 0).
    next : Node
        The next node in the linked list.
    prev : Node
        The previous node in the linked list.
    keys : set
        A set of keys associated with the node.
    """

    def __init__(self, count=0):
        self.count = count
        self.next = None
        self.prev = None
        self.keys = set()