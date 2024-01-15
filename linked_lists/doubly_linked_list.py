from .singly_linked_list import SLLNode


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