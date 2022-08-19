from operator import ne


class Node:
    """
        object which represents only one node
        I implemented node in a way where next points to None
        after creation of object, but this is more helpful for single_linked_list
    """

    def __init__(self,value):
        self.value = value
        self.next = None
    
class Single_linked_list:
    """
        Singly_linked_list object. 
    """
    def __init__(self):
        self.head = None
        self.tail = None 
        self.length = 0 
    

    def insertAtTail(self,node):

        node = Node(node)

        if self.length == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
    

    def insertAtHead(self,node):
        node = Node(node)

        if self.length == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1


    def printerOfArray(self):
        temp = self.head
        for i in range(0,self.length):
            
            print(f"index {i} {temp.value}")
            temp = temp.next

            

    def insertAtIndex(self,node,index):
        node = Node(node)

        temp,n = self.head,0


        if index < 0 or index > self.length:
            raise Exception("Enter correct index! ")

        if index == 0:
            self.insertAtHead(node)
        else:
            while n<index-1:
                temp = temp.next
                n+=1
            
            node.next = temp.next
            temp.next = node

        self.length += 1 



lst = Single_linked_list()

lst.insertAtTail(10)
lst.insertAtTail(20)
lst.insertAtHead(0)

print(lst.printerOfArray())
print(lst.length)

print("___")

lst.insertAtIndex(index=1,node=5)
print(lst.printerOfArray())

print("___")

lst.insertAtIndex(index=4,node=50)
print(lst.printerOfArray())

print("___")

lst.insertAtIndex(index=0,node=506)
print(lst.printerOfArray())