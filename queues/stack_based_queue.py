
class Queue:
    def __init__(self) -> None:
        # enqueue_stack is used to enqueue items
        self.enqueue_stack = []
        # dequeue_stack is used to dequeue items
        self.dequeue_stack = []

    def __len__(self) -> int:
        # the length of the queue is the sum of the lengths of the enqueue_stack and dequeue_stack
        return len(self.enqueue_stack) + len(self.dequeue_stack)
    
    def enqueue(self, item: object) -> None:
        # enqueue items onto the enqueue_stack
        self.enqueue_stack.append(item)

    def dequeue(self) -> object:
        if len(self) == 0:
            raise IndexError("dequeue() called on empty queue.")
        if len(self.dequeue_stack) == 0:
            # if the dequeue_stack is empty, then pop all items off the enqueue_stack and push them onto the dequeue_stack
            while len(self.enqueue_stack) > 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()
    
    def __str__(self) -> str:
        # the string representation of the queue is the concatenation of the enqueue_stack and dequeue_stack
        return str(self.enqueue_stack + self.dequeue_stack)
    

if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue)

    queue.dequeue()

    print(queue)