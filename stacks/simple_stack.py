# a Stack can be easily implemented using the built-in methods of a Python list
stack = []

# push an element onto the stack
stack.append(1)

# to be technically precise, the .insert() method can be used to push an element onto the top (front) of the stack
stack.insert(0, 1)

# pop an element off the stack
stack.pop()

# again, to be technically precise, the .pop(0) method can be used to pop an element off the top (front) of the stack
stack.pop(0)

# peek at the top element of the stack
stack[-1]


# alternatively, a Stack can be implemented as a simple class using the same built-in methods of a Python list
class Stack:
    def __init__(self):
        self.__index = []

    def __len__(self):
        return len(self.__index)

    def push(self, item):
        self.__index.insert(0, item)

    def pop(self):
        if len(self.__index) == 0:
            raise IndexError("pop() called on empty stack.")
        return self.__index.pop(0)
    
    def peek(self):
        if len(self.__index) == 0:
            raise IndexError("peek() called on empty stack.")
        return self.__index[0]
    
    def __str__(self):
        return str(self.__index)