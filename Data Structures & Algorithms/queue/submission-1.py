class listNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = listNode(0)
        self.tail = listNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return True if self.head.next == self.tail else False

    def append(self, value: int) -> None:
        new = listNode(value)
        temp = self.tail.prev
        self.tail.prev = new
        new.next = self.tail
        new.prev = temp
        temp.next = new

    def appendleft(self, value: int) -> None:
        new = listNode(value)
        temp = self.head.next
        self.head.next = new
        new.prev = self.head
        new.next = temp
        temp.prev = new

    def pop(self) -> int:
        if self.head.next != self.tail:
            curr = self.tail.prev
            self.tail.prev = curr.prev
            curr.prev.next = self.tail
            return curr.val
        return -1 

    def popleft(self) -> int:
        if self.head.next != self.tail:
            curr = self.head.next
            self.head.next = curr.next
            curr.next.prev = self.head
            return curr.val
        return -1 
