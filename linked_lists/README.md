# Linked List

A Linked List is a linear data structure that consists of a sequence of nodes. Each node contains a value and a pointer to the next node in the sequence. 

The entry point to a Linked List is called the head. The head is not a separate node, but rather a reference to the first node in the sequence.

The last node in the sequence is called the tail. The tail node's pointer points to `None`.

Linked Lists are also sequential access data structures, meaning that to access a node in the middle of the sequence, the nodes before it must be traversed.

Linked Lists are also recursive data structures, meaning that they are either empty or consist of a node followed by a Linked List.

There are two primary operations on a Linked List:
- Add: add a node to the front or back of the Linked List. It may also be possible to add a node just before or after a node whose value is known (this is called a 'key').
- Remove: remove a node from the front or back of the Linked List. Same as above, it may also be possible to remove a node just before or after a node whose value is known.

A few other operations that may be supported are:
- IsEmpty: check if the Linked List is empty.
- Size: return the number of nodes in the Linked List.
- Search: return the index of a node given its key.

There are two types of Linked Lists:
- Singly Linked List: each node only has a pointer to the next node in the sequence.
- Doubly Linked List: each node has a pointer to the next node and a pointer to the previous node in the sequence.