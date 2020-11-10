class PriorityQueue:
    def __init__(self, compare_function= lambda x, y: x < y):
        self.lst = [None]
        self.count = 0
        self.comp = compare_function
    def __len__(self):
        return len(self.lst) - 1
    def __repr__(self):
        return str(self.lst[1:])
    def __str__(self):
        return str(self.lst[1:])
    def get_left_child(self, index):
        if index * 2 < len(self.lst):
            return index * 2
        return None
    def get_right_child(self, index):
        if index * 2 + 1 < len(self.lst):
            return index * 2 + 1
        return None
    def get_parent(self, index):
        if (parent_index := index // 2) > 0:
            return parent_index
        return None
    def swap(self, i1, i2):
        self.lst[i1], self.lst[i2] = self.lst[i2], self.lst[i1]
    def heapify_up(self):
        index = 1
        while True:
            left = self.get_left_child(index)
            right = self.get_right_child(index)
            if left and right:
                if self.comp(self.lst[left], self.lst[right]):
                    if self.comp(self.lst[left], self.lst[index]):
                        self.swap(index, left)
                        index = left
                    else:
                        break
                else:
                    if self.comp(self.lst[right], self.lst[index]):
                        self.swap(index, right)
                        index = right
                    else:
                        break
            if left:
                if self.comp(self.lst[left], self.lst[index]):
                    self.swap(index, left)
                    index = left
                else:
                    break
            else:
                break
    
    def heapify_down(self):
        index = len(self.lst) - 1
        while True:
            parent_idx = self.get_parent(index)
            if not parent_idx:
                return
            if self.comp(self.lst[index], self.lst[parent_idx]):
                self.swap(index, parent_idx)
                index = parent_idx
            else:
                break
    def enqueue(self, node):
        self.lst.append(node)
        self.heapify_down()
    def dequeue(self):
        if len(self.lst) < 2:
            return
        if len(self.lst) == 2:
            return self.lst.pop()
        self.swap(1, -1)
        value = self.lst.pop()
        self.heapify_up()
        return value

