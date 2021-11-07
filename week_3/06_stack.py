class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return "stack is empty!"
        ptr = self.head
        self.head = self.head.next
        return ptr

    def peek(self):
        if self.is_empty():
            return "stack is empty!"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):

        if self.head is None:
            return True
        else:
            return False


stack = Stack()
stack.push(3)
stack.push(4)
print(stack.peek())
stack.push(7)
print(stack.peek())
stack.pop()
print(stack.peek())
