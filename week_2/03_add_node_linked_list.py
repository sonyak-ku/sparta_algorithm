class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur

    def add_node(self, index, value):
        data = Node(value)  # 집어 넣을 노드
        if index == 0:
            data.next = self.head
            self.head = data
            return

        data.next = self.get_node(index)
        self.get_node(index - 1).next = data


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)

linked_list.add_node(1, 6)
linked_list.add_node(2,20)
linked_list.print_all()