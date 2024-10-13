class Queue:
    def __init__(self):
        self.size = 0
        self.capacity = 3
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def add(self, element):
        if self.is_full():
            raise ValueError('Queue is full')
        self.elements.append(element)
        self.size += 1

    def remove(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        element = self.elements[0]
        for index in range(1, self.size):
            self.elements[index -1] = self.elements[index]
        self.elements.pop()
        self.size -= 1
        return element

    def is_full(self):
        return self.size == self.capacity

    def peek(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        return self.elements[0]

    def retrieve(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        return self.elements[0]

    def offer(self, element):
        if self.is_full():
            return False
        self.elements.append(element)
        self.size += 1
        return True