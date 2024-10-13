class ArrayList:
    def __init__(self):
        self.size = 0
        self.capacity = 3
        self.elements = []

    def is_empty(self):
        return self.size == 0

    def add(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        self.elements.insert(index, element)
        self.size += 1

    def add_at_end(self, element):
        self.elements.append(element)
        self.size += 1
        return True

    def remove_by_index(self, index):
        if self.is_empty():
            raise ValueError("Index out of range")
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        self.elements.pop(index)
        self.size -= 1

    def get_size(self):
        return self.size

    def remove_by_element(self, element):
        if self.is_empty():
            raise ValueError("List is empty")
        for index in range(self.size):
            if self.elements[index] == element:
                self.remove_by_index(index)
                return True
        return False

    def contains(self, element):
        if self.is_empty():
            raise ValueError("List is empty")
        return element in self.elements

    def get(self, index):
        if self.is_empty():
            raise ValueError("List is empty")
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.elements[index]

    def clear(self):
        self.elements = []
        self.size = 0