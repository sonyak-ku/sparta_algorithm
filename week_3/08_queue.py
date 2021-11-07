class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

# [2] -> none
# head   tail
#
# [2] -> [3] -> [4]  -> 5
#               data, next
# head          tail
# [2] -> 3 ->    4  ->5(new)
# head                tail

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def dequeue(self):
        if self.is_empty():
            return "queue is empty!"
        remove_head = self.head
        self.head = self.head.next
        return remove_head.data

    def peek(self):
        if self.is_empty():
            return 'queue is empty!'
        return self.head.data

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False


que = Queue()
que.enqueue(3)
que.enqueue(5)
que.enqueue(7)
print(que.peek().data)
que.dequeue()
print(que.peek().data)
