class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

# Function to print preorder traversal
def preOrder(root):
    if root is not None:
        print(root.data, end = ' ')
        preOrder(root.left)
        preOrder(root.right)

# Function to print inorder traversal
def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root.data, end = ' ')
        inOrder(root.right)

# Function to print postorder traversal
def postOrder(root):
    if root is not None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end = ' ')


# Examples
root = Node(1)
root.left  = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
print('PreOrder Traversal is:')
preOrder(root)
print('\nInOrder Traversal is :')
inOrder(root)
print('\nPostOrder Traversal is:')
postOrder(root)


