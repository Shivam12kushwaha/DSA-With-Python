# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    
    def __init__(self, head=None):
        self.head = head


    # Insert at Beginning
    def insertAtBegin(self, value):
        new_node = Node(value)

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head
        self.head = new_node


    # Insert at End
    def insertAtEnd(self, value):
        new_node = Node(value)

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head


    # Insert in Middle (after a given value x)
    def insertAtMid(self, value, x):
        new_node = Node(value)

        if self.head is None:
            return

        temp = self.head

        while True:

            if temp.data == x:
                new_node.next = temp.next
                temp.next = new_node
                return

            temp = temp.next

            if temp == self.head:
                break


    # Delete a Node
    def deleteNode(self, value):

        if self.head is None:
            return

        temp = self.head
        prev = None

        # Case 1: Deleting head
        if temp.data == value:

            while temp.next != self.head:
                temp = temp.next

            if temp == self.head:
                self.head = None
                return

            temp.next = self.head.next
            self.head = self.head.next
            return

        temp = self.head

        while temp.next != self.head:

            prev = temp
            temp = temp.next

            if temp.data == value:
                prev.next = temp.next
                return


    # Print Circular Linked List
    def printLL(self):

        if self.head is None:
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print()

obj = CircularLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(50)
obj.insertAtBegin(5)
obj.insertAtMid(40, 20)
obj.printLL()
obj.deleteNode(50)
obj.printLL()