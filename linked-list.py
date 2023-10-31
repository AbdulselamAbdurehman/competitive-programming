class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if self.length == 0 or index >= self.length:
            return -1
        curr = self.head
        i = 0
        while i < index:
            if not curr.next:
                return -1
            curr = curr.next
            i += 1
        return curr.val

    def addAtHead(self, val: int) -> None:
        temp = self.head
        self.head = Node(val)
        self.head.next = temp
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.length == 0:
            self.head = Node(val)
            self.length += 1
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        elif self.length == index:
            self.addAtTail(val)
            return
        if index > self.length:
            return
        i = 0
        curr = self.head
        while i < index-1:
            curr = curr.next
            i += 1
        temp = curr.next
        curr.next = Node(val)
        curr.next.next = temp
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        i = 0
        curr = self.head
        while i < index-1:
            i += 1
            curr = curr.next
        curr.next = curr.next.next
        self.length -= 1


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

