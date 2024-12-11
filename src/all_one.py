from node import Node


class AllOne:
    """
    A data structure that supports the following operations:
    - inc(key): Increments the count of the key by 1. If the key does not exist, it is added with count 1.
    - dec(key): Decrements the count of the key by 1. If the key's count becomes 0, it is removed from the data structure.
    - getMaxKey(): Returns one of the keys with the maximum count. If no keys exist, returns an empty string.
    - getMinKey(): Returns one of the keys with the minimum count. If no keys exist, returns an empty string.

    The data structure maintains the keys in a doubly linked list to efficiently support the above operations.

    Attributes:
        first (Node): A dummy head node for the doubly linked list.
        last (Node): A dummy tail node for the doubly linked list.
        key_to_nodes (dict): A dictionary mapping keys to their corresponding nodes in the doubly linked list.
    """

    def __init__(self):
        self.first = Node()
        self.last = Node()
        self.first.next = self.last
        self.last.prev = self.first
        self.key_to_nodes = {}

    def add_node(self, curr_node, node):
        """
        Inserts a new node after the current node in a doubly linked list.

        Args:
            curr_node (Node): The current node after which the new node will be inserted.
            node (Node): The new node to be inserted.
        """
        next_node = curr_node.next
        curr_node.next = node
        node.prev = curr_node
        node.next = next_node
        next_node.prev = node

    def remove_node(self, node):
        """
        Removes a node from a doubly linked list.

        This method updates the pointers of the adjacent nodes to bypass the node
        being removed, effectively removing it from the list.

        Args:
            node (Node): The node to be removed.
        """
        node.next.prev = node.prev
        node.prev.next = node.next

    def inc(self, key: str) -> None:
        """
        Increments the count of the given key in the data structure. If the key does not exist, it is added with a count of 1.
        If the key exists, its count is incremented by 1. The nodes in the data structure are updated accordingly to maintain
        the correct order based on counts.

        Args:
            key (str): The key to be incremented.

        Returns:
            None
        """
        key_node = self.key_to_nodes.get(key)
        if not key_node:
            next_node = self.first.next
            if self.first.next.count == 1:
                next_node.add_key(key)
            else:
                next_node = Node(1)
                next_node.add_key(key)
                self.add_node(self.first, next_node)
            self.key_to_nodes[key] = next_node
        else:
            key_node.remove_key(key)
            next_node = key_node.next
            if next_node.count == key_node.count + 1:
                next_node.add_key(key)
            else:
                next_node = Node(key_node.count + 1)
                next_node.add_key(key)
                self.add_node(key_node, next_node)
            self.key_to_nodes[key] = next_node
            if not key_node.keys:
                self.remove_node(key_node)

    def dec(self, key: str) -> None:
        """
        Decrements the count of the given key in the data structure. If the key's count
        reaches zero, it is removed from the data structure. The function also updates
        the internal linked list of nodes to maintain the correct order of counts.

        Args:
            key (str): The key whose count is to be decremented.

        Returns:
            None
        """
        key_node = self.key_to_nodes.get(key)
        key_node.remove_key(key)
        if key_node.count > 1:
            prev_node = key_node.prev
            if prev_node.count == key_node.count - 1:
                prev_node.add_key(key)
            else:
                prev_node = Node(key_node.count - 1)
                prev_node.add_key(key)
                self.add_node(key_node.prev, prev_node)
            self.key_to_nodes[key] = prev_node
        else:
            del self.key_to_nodes[key]
        if not key_node.keys:
            self.remove_node(key_node)

    def getMaxKey(self) -> str:
        """
        Returns the key with the maximum count in the data structure.

        If the data structure is empty, it returns an empty string.

        Returns:
            str: The key with the maximum count, or an empty string if the data structure is empty.
        """
        if self.last.prev.count != 0:
            return self.last.prev.get_random_key()
        return ""

    def getMinKey(self) -> str:
        """
        Returns the key with the minimum count in the data structure.

        If the data structure is empty, returns an empty string.

        Returns:
            str: The key with the minimum count, or an empty string if the data structure is empty.
        """
        if self.first.next.count != 0:
            return self.first.next.get_random_key()
        return ""
