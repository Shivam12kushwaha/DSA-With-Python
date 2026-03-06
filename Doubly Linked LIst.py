class Node:
    def __init__(self, value = None):
        self.data =  value
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None

    # Insert at the End
    def InsertAtEnd(self, value):
        temp = Node(value)

        if self.head == None:
            self.head = temp
            return

        t = self.head
        while t.next is not None:
            t = t.next
        t.next = temp
        temp.prev = t


    # Insert at Beginning
    def InsertAtBeg(self, value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp


    # Insert in between
    def InsertAtMid(self, value, x):
        t = self.head
        while t.next is not None:
            if t.data == x:
                break
            else:
                t = t.next
        
        temp = Node(value)
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t


    # Delete a node

    def deleteDLL(self, value):
        if self.head == None:
            print('Linked List is empty.')
            return

        # Deletion from beginning
        t = self.head
        if t.data == value:
            self.head = t.next
            self.head.prev = None
            return
        # Deletion in between
        while t.next is not None:
            if t.data == value:
                t.prev.next = t.next
                return
            else:
                t = t.next

        # Deletion at the End
        if t.data == value:
            t.prev.next = None


    # Print Doubly Linked List
    def printDLL(self):
        t1 = self.head
        while t1.next is not None:
            print(t1.data, end = ' <--> ')
            t1 = t1.next
        print(t1.data) 



# Examples:
obj = DoublyLL()
obj.InsertAtEnd(10)
obj.InsertAtEnd(20)
obj.InsertAtEnd(30)
obj.InsertAtBeg(5)
obj.InsertAtMid(50,20)
obj.printDLL()
obj.deleteDLL(30)
obj.printDLL()