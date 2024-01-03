
class Queue:
    def __init__(self) -> None:
        self.enqueue_stack = []
        self.dequeue_stack = []

    def __len__(self) -> int:
        return len(self.enqueue_stack) + len(self.dequeue_stack)
    
    def enqueue(self, item) -> None:
        self.enqueue_stack.append(item)

    def dequeue(self) -> object:
        if len(self) == 0:
            raise IndexError("dequeue() called on empty queue.")
        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) > 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()
    
    def __str__(self) -> str:
        return str(self.enqueue_stack + self.dequeue_stack)
    

if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue)

    queue.dequeue()

    print(queue)