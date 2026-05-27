#Double link list and Hashmap apporach
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cacheMap = {}
        self.headNode = Node(0, 0)
        self.tailNode = Node(0, 0)
        self.headNode.next = self.tailNode
        self.tailNode.prev = self.headNode
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cacheMap:
            keyNode = self.cacheMap.get(key)
            self._removeNode(keyNode)
            self._appendNode(keyNode)
            return keyNode.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cacheMap:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                delNode = self.headNode.next
                self._removeNode(delNode)
                self.cacheMap.pop(delNode.key)
                
            newNode = Node(key, value)
            self._appendNode(newNode)
            self.cacheMap[key] = newNode

        else:
            existingNode = self.cacheMap.get(key)
            self._removeNode(existingNode)
            self._appendNode(existingNode)
            existingNode.val = value

            
    def _appendNode(self, node: Node):
        Temp = self.tailNode.prev
        Temp.next = node
        node.prev = Temp
        node.next = self.tailNode
        self.tailNode.prev = node
    
    def _removeNode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev


