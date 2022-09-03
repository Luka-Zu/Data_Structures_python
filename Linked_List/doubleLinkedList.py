class Node:
    """
        object which represents only one node
        I implemented node in a way where next points to None
        after creation of object, but this is more helpful for single_linked_list
    """

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    """
            Doubly_linked_list object.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        """
            Returns number of elements in Linked_List
            It is done in O(1)
        """
        return self.length

    def insert_at_head(self, node):
        """
            Method which adds element at
            the beginning of list in O(1) Time
        """
        node = Node(node)

        if self.length == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1



# x = DoubleLinkedList()
# x.insert_at_head(5)
# x.insert_at_head(3)
# x.insert_at_head(2)
#
#
# print(x.head.value)
# print(x.tail.value)
