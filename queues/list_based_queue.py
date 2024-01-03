# a Queue can be easily implemented using the built-in methods of a Python list
queue = []

# enqueue an element onto the queue
queue.append(1)

# dequeue an element off the queue
queue.pop(0)


# alternatively, a Queue can be implemented as a simple class using the same built-in methods of a Python list
class Queue:
    def __init__(self):
        self.__index = []

    def __len__(self):
        return len(self.__index)

    def enqueue(self, item):
        self.__index.append(item)

    def dequeue(self):
        if len(self.__index) == 0:
            raise IndexError("dequeue() called on empty queue.")
        return self.__index.pop(0)
    
    def __str__(self):
        return str(self.__index)