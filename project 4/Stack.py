from Container import Container

# Stack: First in last out
class Stack(Container):

    def peek(self):
        if not self.is_empty():
            return self._items[-1]

    def pop(self):
        if not self.is_empty():
            return self._items.pop()

# Test method
if __name__ == '__main__':
    testvalues = [1, 2, 3, 4, 5, 6]
    stack = Stack()

    for value in testvalues:
        stack.push(value)

    while not stack.is_empty():
        print(stack.peek())
        print(stack.pop())