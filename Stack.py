class stack:
    def __init__(self):
        self.lst = []

    # Function to find the length of the stack
    def length(self, lst):
        return len(self.lst)
    
    # Function to push the elements
    def push(self, value):
        self.lst.insert(0, value)

    # Function to find the top element
    def peak(self):
        if len(self.lst) == 0:
            raise Exception('Stack is Empty')
        else:
            return self.lst[0]
        
    # Function to delete the element from the top
    def pop(self):
        if len(self.lst) == 0:
            raise Exception('Stack is Empty')
        else:
            return self.lst.pop(0)

    # Function to print the stack    
    def printStack(self):
        if len(self.lst) == 0:
            print("Stack is Empty")
        else:
            print("Stack (top -> bottom):")
            for i in self.lst:
                print(i)


# Examples
obj = stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.printStack()
print('Top Element is :', obj.peak())
print('Top element, we are removing is :', obj.pop())