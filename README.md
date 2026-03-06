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
