
class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def __repr__(self):
        return f"SLLNode object: data={self.data}"


class SLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"SLL object: head={self.head}"

    def is_empty(self):
        """Returns True if the Linked List is empty. Otherwise, returns False."""
        return self.head is None  # self.head == None

    def add_front(self, new_data):
        """Add a Node whose data is the new_data argument to the front of the Linked List."""

        pass

    def size(self):
        """Traverses the Linked List and returns an integer value representing the number of nodes in the Linked List.

        The time complexity is O(n) because every Node in the Linked List must be visited in order to calculate the size of the Linked List.
        """

        pass

    def search(self, data):
        """Traverses the Linked List and returns True if the data searched for is present in one of the Nodes. Otherwise, it returns False.

        The time complexity is O(n) because in the worst case, we have to visit every Node in the list.
        """

        pass

    def remove(self, data):
        """Removes the first occurence of a Node that contains the data argument as its self.data variable. Returns nothing.

        The time complexity is O(n) because in the worst case we have to visit every Node before we find the one we need to remove.
        """

        pass