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

    def insert_at_tail(self, node):
        """
            Method which adds element at
            the end of list in O(1) Time
        """

        node = Node(node)

        if self.length == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def insert_at_index(self, node, index):
        """
            Method which adds element at
            the specific index.
        """
        if index < 0 or index >= self.length:
            raise Exception("Enter valid index!")

        node = Node(node)

        if index < self.length / 2:
            self.__insert_from_right(node, index)
        else:
            self.__insert_from_left(node, index)

    def __insert_from_right(self, node, index):

        cur = self.head
        current_index = 0

        while current_index < index:
            current_index += 1
            cur = cur.next

        if current_index != 0:
            node.prev = cur.prev
            node.next = cur
            cur.prev.next = node
            cur.prev = node
        else:

            cur.prev = node
            node.next = cur

            self.head = node
        self.length += 1

    def __insert_from_left(self, node, index):
        current_index = self.length - 1
        cur = self.tail
        while current_index > index:
            current_index -= 1
            cur = cur.prev

        cur.prev.next = node
        node.prev = cur.prev
        cur.prev = node
        node.next = cur
        self.length += 1

    def delete_at_head(self):
        if self.length == 0:
            return
        if self.length == 1:
            self.head = self.tail = None
            self.length -= 1
        else:
            self.head = self.head.next
            self.length -= 1

    def delete_at_tail(self):
        pass

    def delete_at_index(self, index):
        pass


    def printer(self):
        cur = self.head
        current_index = 0
        while current_index < self.length:
            print(f"Value: {cur.value} Index: {current_index}")
            cur = cur.next
            current_index += 1







# TESTING

# x = DoubleLinkedList()
# x.insert_at_head(5)
# x.insert_at_head(3)
# x.insert_at_head(2)
# x.insert_at_tail(2)
# x.insert_at_tail(1)
# x.printer()
# print("_______")
# x.insert_at_index("test", 0)
#
# while x.length > 0:
#     x.delete_at_head()
#     x.printer()
#     print("_______")

