# Superclass for Queue and Stack

class Container :
    def __init__(self):
        self._items = []

    def size(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) < 1

    def push(self, item):
        self._items.append(item)

    def pop(self):
        raise NotImplementedError
    
    def peek(self):
        raise NotImplementedError
