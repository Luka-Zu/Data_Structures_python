from Linked_List import singleLinkedList

class Stack:
    def __init__(self, starting_elements=None):
        self.elements = singleLinkedList.SingleLinkedList()
        if starting_elements is not None:
            for elem in starting_elements:
                self.elements.insert_at_head(elem)

    def push(self,elem):
        self.elements.insert_at_head(elem)

    def pop(self):
        if self.elements.length <= 0:
            raise Exception("No elements in stack")

        popped = self.elements.head.value
        self.elements.remove_at_head()
        return popped

    def peek(self):
        if self.elements.length <= 0:
            raise Exception("No elements in stack")

        peeked = self.elements.head.value
        return peeked

    def empty(self):
        return self.elements.length == 0


s = Stack(["pirvel", 34])
s.push("a")
s.push("b")

s.push("c")

s.push("d")

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
