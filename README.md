# DSA
DSA stands for Data Structures and Algorithms. Data structures manage how data is stored and accessed. Algorithms focus on processing this data. Examples of data structures are **Array**, **Linked List**, **Tree and Heap**, and examples of algorithms are **Binary Search**, **Quick Sort** and **Merge Sort**.
## (1) Array in Python:
An **Array** is a Linear Data Structure, which is a collection of elements stored in contiguous memory collections.
### Advantages:
* Efficient and Fast access.
* Memory Efficiency
* Versatility
* Compatibiltity with hardwares.
## (2) Linked List:
A linked list is a type of linear data structure individual items are not necessarily at cintiguous locations. The individual items are called **Nodes** and they are coonected through **Links**.
* A Node is contains two things first thing is **Data** and other is a **Link** that conncects it with other node.
* The first node is called **Head** and we can traverse the whole node using this head and next links.
### Types of Linked List:
(i) Singly Linked List
(ii) Doubly Linked List
(iii) Circular Linked List
### Singly Linked List:
A singly linked list is a fundamental data structure, it consists of nodes where each node contains a data field and a reference to the next node in the linked list. The next of the last node is null, indicating the end of the list. Linked Lists support efficient insertion and deletion operations.
### Doubly Linked List:
A doubly linked list is a more complex data structure than a singly linked list, but it offers several advantages. The main advantage of a doubly linked list is that it allows for efficient traversal of the list in both directions. This is because each node in the list contains a pointer to the previous node and a pointer to the next node. This allows for quick and easy insertion and deletion of nodes from the list, as well as efficient traversal of the list in both directions.
A doubly linked list is represented using nodes that have three fields:
* Data
* A pointer to the next node (**next**)
* A pointer to the previous node (**prev**)
### Advantages of Doubly Linked List:
* Bidirectional Traversal
* Efficient Deletion
* Insertion at Both Ends
### Disadvantages of Doubly Linked List:
* Extra Memory Per Node
* More Complex Implementation
* Slower Operations Due to Overhead
* Not Cache friendly
### Circular Linked List:
A circular linked list is a data structure where the last node points back to the first node, forming a closed loop.
* **Structure:** All nodes are connected in a circle, enabling continuous traversal without encountering NULL.
* Difference from Regular Linked List: In a regular linked list, the last node points to NULL, whereas in a circular linked list, it points to the first node.
* **Uses:** Ideal for tasks like scheduling and managing playlists, where smooth and repeated.
### Types of Circular Linked Lists:
**(i) Circular Singly Linked List:** In Circular Singly Linked List, each node has just one pointer called the "next" pointer. The next pointer of the last node points back to the first node and this results in forming a circle. In this type of Linked list, we can only move through the list in one direction.

**(ii) Circular Doubly Linked List:** In circular doubly linked list, each node has two pointers prev and next, similar to doubly linked list. The prev pointer points to the previous node and the next points to the next node. Here, in addition to the last node storing the address of the first node, the first node will also store the address of the last node.
### Advantage of Circular Linked List:
* Efficient Traversal
* No Null Pointers / References
* Useful for Repetitive Tasks
* Insertion at Beginning or End is O(1)
* Uniform Traversal
* Efficient Memory Utilization
### Disadvantage of Circular Linked List:
* Complex Implementation
* Infinite Loop Risk
* Harder to Debug
* Deletion Complexity
* Memory Overhead (for Doubly Circular LL)
* Not Cache Friendly
## (3)  Stack:
A Stack is a linear data structure that follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out). LIFO implies that the element that is inserted last, comes out first and FILO implies that the element that is inserted first, comes out last.
### Basic Terminologies of Stack:
* **Top:** The position of the most recently inserted element. Insertions (push) and deletions (pop) are always performed at the top.
* **Size:** Refers to the current number of elements present in the stack.
### Types of Stack:
### (i) Fixed Size Stack:
* A fixed size stack has a predefined capacity.
* Once it becomes full, no more elements can be added (this causes overflow).
* If the stack is empty and we try to remove an element, it causes underflow.
* Typically implemented using a static array.
### (ii) Dynamic Size Stack:
* A dynamic size stack can grow and shrink automatically as needed.
* If the stack is full, its capacity expands to allow more elements.
* As elements are removed, memory usage can shrink as well.
* Can be implemented using:
  * -> Linked List → grows/shrinks naturally.
  * -> Dynamic Array (like vector in C++ or ArrayList in Java) → resizes automatically.
### Common Operations on Stack:
In order to make manipulations in a stack, there are certain operations provided to us.
* **push():** to insert an element into the stack.
* **pop():** to remove an element from the stack.
* **top():** Returns the top element of the stack.
* **isEmpty():** returns true if stack is empty else false.
* **size():** returns the size of the stack.
## (4) Queue:
Queue is a linear data structure that follows **FIFO (First In First Out)** Principle, so the first element inserted is the first to be popped out.
### Basic Terminologies of Queue:
 * **Front:** Position of the entry in a queue ready to be served, that is, the first entry that will be removed from the queue, is called the front of the queue. It is also referred as the head of the queue.
 * **Rear:** Position of the last entry in the queue, that is, the one most recently added, is called the rear of the queue. It is also referred as the tail of the queue.
 * **Size:** Size refers to the current number of elements in the queue.
 * **Capacity:** Capacity refers to the maximum number of elements the queue can hold.
### Types of Queues:
Queue data structure can be classified into 3 types:
### (i) Simple Queue:
A simple queue follows the FIFO (First In, First Out) principle.
 * Insertion is allowed only at the rear (back).
 * Deletion is allowed only from the front.
 * Can be implemented using a linked list or a circular array.
### (ii) Double-Ended Queue (Deque):
In a deque, insertion and deletion can be performed from both ends.
### (iii) Priority Queue:
A queue where each element is assigned a priority, and deletion always happens based on priority (not just position).
### Queue Operations:
 * **Enqueue:** Adds an element to the end (rear) of the queue. If the queue is full, an overflow error occurs.
 * **Dequeue:** Removes the element from the front of the queue. If the queue is empty, an underflow error occurs.
 * **Peek/Front:** Returns the element at the front without removing it.
 * **Size:** Returns the number of elements in the queue.
 * **isEmpty:** Returns true if the queue is empty, otherwise false.
 * **isFull:** Returns true if the queue is full, otherwise false.
### Advantages of Queue:
* Queues are useful when a particular service is used by multiple consumers.
* Queues are fast in speed for data inter-process communication.
* Queues can be used for the implementation of other data structures.
### Disadvantages of Queue:
* The operations such as insertion and deletion of elements from the middle are time consuming.
* In a classical queue, a new element can only be inserted when the existing elements are deleted from the queue.
* Searching an element takes O(N) time.
* Maximum size of a queue must be defined prior in case of array implementation.
## (5) Deque:
Deque or Double Ended Queue is a generalized version of Queue data structure that allows insert and delete at both ends.
* Deque can act as both Stack and Queue
* It is useful in many problems where we need to have a subset of all operations also like insert/remove at front and insert/remove at the end.
* It is typically implemented either using a doubly linked list or circular array.
## (6) Recursion:
Recursion is a technique used in computer science to solve big problems by breaking them into smaller, similar problems. The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called a **Recursive Function**. Using a recursive algorithm, certain problems can be solved quite easily.
Recursive function contains two key parts:
* **Base Case:** The stopping condition that prevents infinite recursion.
* **Recursive Case:** The part of the function where it calls itself with modified parameters.
### Steps to Implement Recursion:
* (i) Define a base case
* (ii) Define a recursive case
* (iii) Ensure the recursion termination
* (iv) Combine the solution

## (7) Tree:
Tree Data Structure is a non-linear data structure in which a collection of elements known as nodes are connected to each other via edges such that there exists exactly one path between any two nodes. The topmost node is called the root, and every other node can have one or more child nodes.
### Basic Terminologies In Tree Data Structure:
* **Parent Node:** A node that is an immediate predecessor of another node.
* **Child Node:** A node that is an immediate successor of another node.
* **Root Node:** The topmost node in a tree, which does not have a parent. 
* **Leaf Node (External Node):** Nodes that do not have any children.
* **Ancestor:** Any node on the path from the root to a given node (excluding the node itself).
* **Descendant:** A node x is a descendant of another node y if y is an ancestor of x. 
* **Sibling:** Nodes that share the same parent. 
* **Level of a Node:** The number of edges in the path from the root to that node.The root node is at level 0.
* **Internal Node:** A node with at least one child.
* **Neighbor of a Node:** The parent or children of a node.
* **Subtree:**  A node and all its descendants form a subtree.
### Why Tree is considered a non-linear data structure?
Data in a tree is not stored sequentially (i.e., not in a linear order). Instead, it is organized across multiple levels, forming a hierarchical structure. Because of this arrangement, a tree is classified as a non-linear data structure.

### Importance of Tree Data Structure:
* Trees are useful for storing data that naturally forms a hierarchy.
* File systems on computers are structured as trees, with folders containing subfolders and files.
* The DOM (Document Object Model) of an HTML page is a tree:The <html> tag is the root.<head> and <body> are its children.These tags can have their own child nodes, forming a hierarchical structure.
* Trees help in efficient data organization and retrieval for hierarchical relationships.
### Types of Tree Data Structures :
Tree data structures can be classified based on the number of children each node can have.
### Binary Tree:
Each node can have a maximum of two children.
* **Full Binary Tree** – every node has either 0 or 2 children.
* **Complete Binary Tree** – all levels are fully filled except possibly the last, which is filled from left to right.
* **Balanced Binary Tree** – height difference between left and right subtrees of every node is minimal.
### Ternary Tree:
Each node can have at most three children, often labeled as left, middle, and right.

### N-ary Tree (or Generic Tree):
* Each node can have any number of children.
* Each node typically contains: Some data , A list of references to its children (duplicates are not allowed).
* Unlike linked lists, nodes store references to multiple child nodes.

### Properties of Tree Data Structure:
* **Number of edges:** An edge is the connection between two nodes. A tree with N nodes will always have N - 1 edges. There is exactly one path from any node to any other node in the tree.
* **Depth of a node:** The depth of a node is the length of the path from the root to that node. Each edge in the path adds 1 unit to the length. Equivalently, it is the number of edges from the root to the node.
* **Height of the tree:** The height of the tree is the length of the longest path from the root to any leaf node.
* **Degree of a node:** The degree of a node is the number of subtrees attached to it (i.e., the number of children it has).
* A leaf node has a degree of 0.
* The degree of the tree is the maximum degree among all nodes in the tree.

## (8) Graph:
Graph is a non-linear data structure like tree data structure. A Graph is composed of a set of **vertices(V)** and a set of **edges(E)**. The vertices are connected with each other through edges.
* The limitation of tree is, it can only represent hierarchical data. For situations where nodes or vertices are randomly connected with each other other, we use Graph.
### Representations of Graph:
Here are the two most common ways to represent a graph-
* (i) Adjacency Matrix
* (ii) Adjacency List
### (i) Adjacency Matrix Representation:
An adjacency matrix is a way of representing a graph as a boolean matrix of (0's and 1's).
Let's assume there are n vertices in the graph So, create a 2D matrix adjMat[n][n] having dimension n x n.
* If there is an edge from vertex i to j, mark adjMat[i][j] as 1. 
* If there is no edge from vertex i to j, mark adjMat[i][j] as 0.
### (ii) Adjacency List Representation:
An array of Lists is used to store edges between two vertices. The size of array is equal to the number of vertices (i.e, n). Each index in this array represents a specific vertex in the graph. The entry at the index i of the array contains a linked list containing the vertices that are adjacent to vertex i. Let's assume there are n vertices in the graph So, create an array of list of size n as adjList[n].
* adjList[0] will have all the nodes which are connected (neighbour) to vertex 0.
* adjList[1] will have all the nodes which are connected (neighbour) to vertex 1 and so on.
### Depth First Search:
Depth First Search (DFS) is a graph traversal method that starts from a source vertex and explores each path completely before backtracking and exploring other paths. To avoid revisiting nodes in graphs with cycles, a visited array is used to track visited vertices.

**Note:** There can be multiple DFS traversals of a graph according to the order in which we pick adjacent vertices.
**Depth First Search (DFS) starts from a given source vertex and explores one path as deeply as possible. When it reaches a vertex with no unvisited neighbors, it backtracks to the previous vertex to explore other unvisited paths. This continues until all vertices reachable from the source are visited.
In a graph, there might be loops. So we use an extra visited array to make sure that we do not process a vertex again.**

**Time complexity:** O(V + E), where V is the number of vertices and E is the number of edges in the graph.

**Auxiliary Space:** O(V + E), since an extra visited array of size V is required, And stack size for recursive calls to dfsRec function.
### DFS of a Disconnected Graph:
In a disconnected graph, some vertices may not be reachable from a single source. To ensure all vertices are visited in DFS traversal, we iterate through each vertex, and if a vertex is unvisited, we perform a DFS starting from that vertex being the source. This way, DFS explores every connected component of the graph.
### Breadth First Search:
Breadth First Search (BFS) is a graph traversal algorithm that starts from a source node and explores the graph level by level. First, it visits all nodes directly adjacent to the source. Then, it moves on to visit the adjacent nodes of those nodes, and this process continues until all reachable nodes are visited.
* BFS is different from DFS in a way that closest vertices are visited before others. We mainly traverse vertices level by level.
* Popular graph algorithms like **Dijkstra's shortest path, Kahn's Algorithm, and Prim's algorithm** are based on BFS.
* BFS itself can be used to detect cycle in a directed and undirected graph, find shortest path in an unweighted graph and many more problems.

**The algorithm starts from a given source vertex and explores all vertices reachable from that source, visiting nodes in increasing order of their distance from the source, level by level using a queue. Since graphs may contain cycles, a vertex could be visited multiple times. To prevent revisiting a vertex, a visited array is used.**

**Time Complexity:** O(V + E), BFS explores all the vertices and edges in the graph. It visits every vertex and edge only once.

**Auxiliary Space:** O(V), Using a queue to keep track of the vertices that need to be visited.

**In a disconnected graph, some vertices may not be reachable from a single source. To ensure all vertices are visited in BFS traversal, we iterate through each vertex, and if any vertex is unvisited, we perform a BFS starting from that vertex being the source. This way, BFS explores every connected component of the graph.**

### Applications of BFS in Graphs:
BFS has various applications in graph theory and computer science, including:
* Shortest Path Finding
* Cycle Detection
* Connected Components
* Network Routing

## (9) Sorting:
A Sorting Algorithm is used to rearrange a given array or list of elements in an order.

**Sorting refers to rearrangement of a given array or list of elements according to a comparison operator on the elements. The comparison operator is used to decide the new order of elements in the respective data structure.**
### Types of Sorting Techniques:
There are various sorting algorithms are used in data structures. The following two types of sorting algorithms can be broadly classified:
* **Comparison-based:** We compare the elements in a comparison-based sorting algorithm)
* **Non-comparison-based:** We do not compare the elements in a non-comparison-based sorting algorithm)
### (i) Bubble Sort:
It is a simple sorting algorithm that repeatedly swaps adjacent elements if they are in the wrong order. It performs multiple passes through the array, and in each pass, the largest unsorted element moves to its correct position at the end.
After each pass, we ignore the last sorted elements and continue comparing and swapping remaining adjacent pairs. After k passes, the last k elements are sorted.

**Time Complexity:**  O(n^2)  
**Space Complexity:**  O(1)
### (ii) Insertion Sort:
Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list. It is like sorting playing cards in your hands. You split the cards into two groups: the sorted cards and the unsorted cards. Then, you pick a card from the unsorted group and put it in the right place in the sorted group.
* Start with the second element as the first element is assumed to be sorted.
* Compare the second element with the first if the second is smaller then swap them.
* Move to the third element, compare it with the first two, and put it in its correct position
* Repeat until the entire array is sorted.
### Time Complexity:
* **Best case: O(n)**, If the list is already sorted, where n is the number of elements in the list.
* **Average case: O(n^2)**, If the list is randomly ordered
* **Worst case: O(n^2)**, If the list is in reverse order
### Space Complexity:
* **Auxiliary Space: O(1)**, Insertion sort requires O(1) additional space, making it a space-efficient sorting algorithm.
### Advantages:
* Simple and easy to implement.
* Stable sorting algorithm.
* Efficient for small lists and nearly sorted lists.
* Space-efficient as it is an in-place algorithm.
* Adoptive. the number of inversions is directly proportional to number of swaps. For example, no swapping happens for a sorted array and it takes O(n) time only.
### Disadvantages:
* Inefficient for large lists.
* Not as efficient as other sorting algorithms (e.g., merge sort, quick sort) for most cases.
### Applications of Insertion Sort:
Insertion sort is commonly used in situations where:
 * The list is small or nearly sorted.
 * Simplicity and stability are important.
 * Used as a subroutine in Bucket Sort
 * Can be useful when array is already almost sorted (very few inversions)
 * Since Insertion sort is suitable for small sized arrays, it is used in Hybrid Sorting algorithms along with other efficient algorithms like Quick Sort and Merge Sort. 
When the subarray size becomes small, we switch to insertion sort in these recursive algorithms. For example IntroSort and TimSort use insertions sort.
### (iii) Selection Sort:
 Selection Sort is a comparison-based sorting algorithm. It sorts by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element.
* Find the smallest element and swap it with the first element. This way we get the smallest element at its correct position.
* Then find the smallest among remaining elements (or second smallest) and swap it with the second element.
* We keep doing this until we get all elements moved to correct position.
### Time Complexity: O(n^2)
One loop to select an element of Array one by one = O(n)
Another loop to compare that element with every other Array element = O(n)
Therefore overall complexity = O(n) * O(n) = O(n*n) = O(n^2)
### Auxiliary Space: O(1)
### Advantages of Selection Sort:
* Easy to understand and implement, making it ideal for teaching basic sorting concepts.
* Requires only a constant O(1) extra memory space.
* It requires less number of swaps (or memory writes) compared to many other standard algorithms. Only cycle sort beats it in terms of memory writes. Therefore it can be simple algorithm choice when memory writes are costly.
### Disadvantages of the Selection Sort:
* Selection sort has a time complexity of O(n^2) makes it slower compared to algorithms like Quick Sort or Merge Sort.
* Does not maintain the relative order of equal elements which means it is not stable.
### Applications of Selection Sort:
* Perfect for teaching fundamental sorting mechanisms and algorithm design.
* Suitable for small lists where the overhead of more complex algorithms isn't justified and memory writing is costly as it requires less memory writes compared to other standard sorting algorithms.
* Heap Sort algorithm is based on Selection Sort.



