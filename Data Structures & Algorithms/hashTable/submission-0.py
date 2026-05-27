class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable:
    
    def __init__(self, capacity: int):
        self.map = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def insert(self, key: int, value: int) -> None:
        index = key % self.capacity
        while self.map[index] != None:
            if self.map[index].key == key:
                self.map[index].val = value
                return
            index += 1
            index %= self.capacity

        newNode = Pair(key, value)
        self.map[index] = newNode
        self.size += 1

        # resize when the load factor reaches or exceeds 0.5
        if self.size >= self.capacity // 2:
            self.resize()
        
    def get(self, key: int) -> int:
        index = key % self.capacity
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1 
            index %= self.capacity
        return -1

    def remove(self, key: int) -> bool:
        index = key % self.capacity
        while self.map[index] != None:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return True
            index += 1 
            index %= self.capacity
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        #Double capacity
        self.capacity *= 2
        oldMap = self.map
        self.map = [None] * self.capacity
        #Rehash the hashmap
        for node in oldMap:
            if not node:
                continue
            index = node.key % self.capacity
            while self.map[index] != None:
                index += 1
                index %= self.capacity
            self.map[index] = node
        

