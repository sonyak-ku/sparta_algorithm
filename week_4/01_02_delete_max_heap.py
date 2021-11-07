class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        deleted_item = self.items.pop()

        cur = 1
        max_index = len(self.items) - 1
        while cur * 2 <= max_index or (cur * 2 + 1) <= max_index:
            if (cur * 2 + 1) <= max_index:
                if self.items[cur * 2] >= self.items[cur * 2 + 1]:
                    self.items[cur], self.items[cur * 2] = self.items[cur * 2], self.items[cur]
                    cur = cur * 2
                else:
                    self.items[cur], self.items[cur * 2 + 1] = self.items[cur * 2 + 1], self.items[cur]
                    cur = cur * 2 + 1
            elif cur*2 <= max_index:
                if self.items[cur * 2] > self.items[cur]:
                    self.items[cur], self.items[cur * 2] = self.items[cur * 2], self.items[cur]
                    cur = cur * 2

        return deleted_item# 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]