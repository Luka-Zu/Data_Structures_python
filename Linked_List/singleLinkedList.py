class Node:
    """
        object which represents only one node
        I implemented node in a way where next points to None
        after creation of object, but this is more helpful for single_linked_list
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList:
    """
        Singly_linked_list object. 
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
            self.tail = node
        self.length += 1

    def insert_at_head(self, node):
        """
            Method which adds element at 
            the beggining of list in O(1) Time
        """
        node = Node(node)

        if self.length == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def printer_of_array(self):
        """
            method which visualise a linked list
            O(N) Time
        """
        temp = self.head
        print(self.length)
        for i in range(0, self.length):
            print(f"index {i} {temp.value}")
            temp = temp.next

    def insert_at_index(self, node, index):
        """
            Method which adds element at
            certain index in o(N) time
        """
        temp, n = self.head, 0

        if index < 0 or index > self.length:
            raise Exception("Enter correct index! ")

        if index == 0:
            self.insertAtHead(node)
        else:
            node = Node(node)

            while n < index - 1:
                temp = temp.next
                n += 1

            node.next = temp.next
            temp.next = node
            self.length += 1

    def remove_at_head(self):
        """
            Method which removes element at
            the beggining  in o(1) time
        """
        if self.length == 0:
            self.head = self.tail = None
        elif self.length == 1:
            self.head = self.tail = None
            self.length -= 1
        else:
            self.head = self.head.next
            self.length -= 1

    def remove_at_tail(self):
        """
            Method which removes element at
            the end  in o(1) time
        """
        if self.length == 0:
            self.head = self.tail = None
        elif self.length == 1:
            self.head = self.tail = None
            self.length -= 1
        else:

            cur = self.head
            while cur.next.next != None:
                cur = cur.next
            self.tail = cur
            cur.next = None
            self.length -= 1

    def remove_at_index(self, index):
        """
            Method which removes element at
            the index  in o(N) time
        """
        if index < 0 or index > self.length:
            raise Exception("Enter correct index! ")

        if self.length == 0:
            self.head = self.tail = None
        elif self.length == 1:
            self.head = self.tail = None
            self.length -= 1
        else:
            if index == 0:
                self.head = self.head.next
                self.length -= 1
                return

            cur = self.head
            curIndex = 0
            while curIndex + 1 < index:
                curIndex += 1
                cur = cur.next
            cur.next = cur.next.next
            self.length -= 1
