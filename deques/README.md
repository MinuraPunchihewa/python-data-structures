# Deques

A Deque is a double-ended queue.  It is a data structure that supports insertion and deletion at both the front and back of the queue. Therefore, it is neither a FIFO nor a LIFO data structure, but a hybrid of the two.

The programmer can enforce the behavior of the Deque (FIFO or LIFO) by only using the appropriate methods. Essentially, a Deque can be used as a Stack or a Queue.

The `collections` module in Python provides a `deque` class that implements a Deque. It is specifically optimized for fast (and memory-efficient) appends and pops from both ends.

In addition to the operations of adding and removing elements from the front and back of the Deque, the following operations are also typically supported:
- Reverse: reverse the order of the elements in the Deque.
- Rotate: rotate the elements in the Deque by a specified number of steps.  If the number of steps is positive, the elements are rotated to the right.  If the number of steps is negative, the elements are rotated to the left.
- Extend: extend the Deque by appending elements from an iterable to the right.