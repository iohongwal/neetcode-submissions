class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [0] * capacity

    def get(self, i: int) -> int:
        if i < self.capacity:
            return self.array[i] 
        return None

    def set(self, i: int, n: int) -> None:
        if i < self.capacity:
            self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        tail = self.array[self.length - 1]
        self.length -= 1
        return tail

    def resize(self) -> None:
        self.capacity *= 2
        newArray = [0] * self.capacity
        for i, num in enumerate(self.array):
            newArray[i] = num
        self.array = newArray

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
