
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
    

class DLLNode(SLLNode):
    def __init__(self, data):
        super().__init__(data)
        self.previous = None
    
    def get_previous(self):
        return self.previous
    
    def set_previous(self, new_previous):
        self.previous = new_previous
    
    def __repr__(self):
        return f"DLLNode object: data={self.data}"