class Node:
    """
        object which represents only one node
        I implemented node in a way where next points to None
        after creation of object, but this is more helpful for single_linked_list
    """

    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    pass