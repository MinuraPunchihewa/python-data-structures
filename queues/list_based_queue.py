# a Queue can be easily implemented using the built-in methods of a Python list
queue = []

# enqueue an element onto the queue
queue.append(1)

# dequeue an element off the queue
queue.pop(0)


# alternatively, a Queue can be implemented as a simple class using the same built-in methods of a Python list
class Queue:
    def __init__(self) -> None:
        self.__index = []

    def __len__(self) -> int:
        return len(self.__index)

    def enqueue(self, item: object) -> None:
        self.__index.append(item)

    def dequeue(self) -> object:
        if len(self.__index) == 0:
            raise IndexError("dequeue() called on empty queue.")
        return self.__index.pop(0)
    
    def __str__(self) -> str:
        return str(self.__index)
    

if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue)

    queue.dequeue()

    print(queue)