from collections import deque


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        # give value to callback (pre-order)
        cb(self.value)
        # check the left
        if self.left:
            self.left.depth_first_for_each(cb)
        # check the right
        if self.right:
            self.right.depth_first_for_each(cb)

    def breadth_first_for_each(self, cb):
        # create queue (FIFO)
        queue = deque()
        # add first el to queue
        queue.append(self)
        # while queue is not empty
        while queue:
            # remove from front of queue
            popped = queue.popleft()
            # pass into callback
            cb(popped.value)
            # if children (left and right) exist, add to queue
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if (value < self.value):
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value
