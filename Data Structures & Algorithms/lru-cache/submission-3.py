class LRUCache:

    def __init__(self, capacity: int):
        self.cacheMap = {}
        self.cacheStack = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cacheMap:
            self.cacheStack.remove(key)
            self.cacheStack.append(key)
            return self.cacheMap[key]

        return  -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cacheMap: 
            if self.capacity > 0:
                self.capacity -= 1
            else:
                leastKey = self.cacheStack.pop(0)
                self.cacheMap.pop(leastKey)
            self.cacheStack.append(key)
        else:
            self.cacheStack.remove(key)
            self.cacheStack.append(key)
            
        self.cacheMap[key] = value
