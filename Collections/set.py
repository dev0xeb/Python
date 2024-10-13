class Set:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.elements = []

    def is_empty(self):
        return self.size == 0

    def add(self, element):
        if element in self.elements:
            raise ValueError("Element already present in set")
        if self.size < self.capacity:
            self.elements.append(element)
            self.size += 1
            return True
        else:
            raise ValueError("Set is full")

    def remove(self, element):
        if self.is_empty():
            raise ValueError("Set is empty")
        for index in range(self.size):
            if self.elements[index] == element:
                self.elements.pop(index)
                self.size -= 1
                return True
        return False

    def get_size(self):
        return self.size

    def contains(self, element):
        if not self.is_empty():
            if element in self.elements:
                return True
            return False
        raise ValueError("Set is empty")

    def is_full(self):
        return self.size == self.capacity

    def clear(self):
        self.size = 0