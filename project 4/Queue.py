from Container import Container

# Queue: First in first out
class Queue(Container):

    def peek(self):
        if not self.is_empty():
            return self._items[0]

    def pop(self):
        if not self.is_empty():
            return self._items.pop(0)

# Test method
if __name__ == '__main__':
    testvalues = [1, 2, 3, 4, 5, 6]
    queue = Queue()

    for value in testvalues:
        queue.push(value)

    while not queue.is_empty():
        print(queue.peek())
        print(queue.pop())