
class Node:
    def __init__(self, data: object) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = self.rear = None

    def enqueue(self, item: object) -> None:
        temp = Node(item)

        # if queue is empty, then new node is front and rear both
        if self.rear is None:
            self.front = self.rear = temp
            return

        # add the new node at the end of queue and change rear
        self.rear.next = temp
        self.rear = temp

    def dequeue(self) -> object:
        # if queue is empty, then return None
        if self.front is None:
            return None

        # store previous front and move front one node ahead
        temp = self.front
        self.front = temp.next

        # if front becomes None, then change rear also as None
        if self.front is None:
            self.rear = None
        return temp.data
    
    def __str__(self) -> str:
        if self.front is None:
            return "Queue is empty."
        else:
            temp = self.front
            result = ""
            while temp is not None:
                result += str(temp.data) + " "
                temp = temp.next
            return result
        
        
if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue)

    queue.dequeue()

    print(queue)
