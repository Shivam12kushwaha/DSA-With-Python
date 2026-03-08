# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:

    def __init__(self):
        self.head = None


    # Insert at Beginning
    def insertAtBegin(self, value):
        new_node = Node(value)

        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            return

        last = self.head.prev

        new_node.next = self.head
        new_node.prev = last

        last.next = new_node
        self.head.prev = new_node

        self.head = new_node


    # Insert at End
    def insertAtEnd(self, value):
        new_node = Node(value)

        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            return

        last = self.head.prev

        last.next = new_node
        new_node.prev = last

        new_node.next = self.head
        self.head.prev = new_node


    # Insert in Middle (after a given value x)
    def insertAtMiddle(self, value, x):
        if self.head is None:
            return

        temp = self.head

        while True:

            if temp.data == x:

                new_node = Node(value)

                new_node.next = temp.next
                new_node.prev = temp

                temp.next.prev = new_node
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

        # Case: deleting head
        if temp.data == value:

            if temp.next == self.head:
                self.head = None
                return

            last = self.head.prev

            self.head = self.head.next
            self.head.prev = last
            last.next = self.head
            return


        temp = self.head.next

        while temp != self.head:

            if temp.data == value:

                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return

            temp = temp.next


    # Print List
    def printList(self):

        if self.head is None:
            return

        temp = self.head

        while True:
            print(temp.data, end=" <--> ")
            temp = temp.next

            if temp == self.head:
                break

        print()

obj     = CircularDoublyLinkedList()

obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)

obj.insertAtBegin(5)

obj.insertAtMiddle(15, 10)

obj.printList()

obj.deleteNode(20)

obj.printList()