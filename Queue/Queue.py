from Linked_List import Double_Linked_List


class Queue:
    def __init__(self, elements=None):
        self.elements = Double_Linked_List.DoubleLinkedList()
        if elements is not None:
            for elem in elements:
                self.enqueue(elem)

    def enqueue(self, elem):
        self.elements.insert_at_tail(elem)

    def dequeue(self):
        if self.is_empty():
            raise Exception("No elements to be peeked!")
        dequeued = self.elements.head
        self.elements.delete_at_head()
        return dequeued

    def length(self):
        return self.elements.length

    def is_empty(self):
        return 0 == self.length()

    def peek(self):
        if self.is_empty():
            raise Exception("No elements to be peeked!")
        peeked = self.elements.head
        return peeked

