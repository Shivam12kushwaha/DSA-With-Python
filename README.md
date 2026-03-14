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

