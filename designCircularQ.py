class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.length = 0
        self.head = self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.length += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty() :
            return False
        if self.head == self.tail:
            self.tail = self.tail.next
        self.head = self.head.next
        self.length -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.size

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
