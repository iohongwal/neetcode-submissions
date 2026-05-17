class listNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = listNode(0)
    
    def get(self, index: int) -> int:
        curr = self.head.next
        for _ in range(index):
            if curr:
                curr = curr.next
        if curr:   
            return curr.val
        return -1

    def insertHead(self, val: int) -> None:
        newNode = listNode(val)
        newNode.next = self.head.next
        self.head.next = newNode

    def insertTail(self, val: int) -> None:
        newNode = listNode(val)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode

    def remove(self, index: int) -> bool:
        curr = self.head
        for _ in range(index):
            if curr:
                curr = curr.next
        if curr and curr.next:
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        valList = []
        while curr:
            valList.append(curr.val)
            curr = curr.next
        return valList