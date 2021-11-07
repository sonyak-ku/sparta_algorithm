class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.front = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)
        cur.next.front = cur

    def get_kth_node_from_last(self, k):
        last_node = self.head
        while last_node.next:
            last_node = last_node.next  #마지막 노드에 접근.
        last_kth_node = last_node

        for i in range(1, k+1):
            if i > 1:
                last_kth_node = last_kth_node.front

        return last_kth_node





linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!