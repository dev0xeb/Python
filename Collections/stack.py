class Stack:
    def __init__(self):
        self.elements = []
        self.size = None
        self.capacity:int = 3

    def is_empty(self):
        return len(self.elements) == 0

    def push(self, element):
        if self.is_full():
            raise ValueError("Stack is full")
        self.elements.append(element)

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        self.elements.pop()


    def capacity(self):
        return self.capacity


    def get_size(self):
        return len(self.elements)


    def is_full(self):
        return len(self.elements) == self.capacity


    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.elements[-1]


    def search(self, element):
        if self.is_empty():
            raise ValueError("Stack is empty")
        for index in range(len(self.elements)):
            if self.elements[index] == element:
             return index
        return -1
