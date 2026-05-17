class Deque:
    
    def __init__(self):
        self.que = []

    def isEmpty(self) -> bool:
        return True if len(self.que) == 0 else False

    def append(self, value: int) -> None:
        self.que.append(value)        

    def appendleft(self, value: int) -> None:
        self.que = [value] + self.que

    def pop(self) -> int:
        return self.que.pop() if len(self.que) else -1

    def popleft(self) -> int:
        return self.que.pop(0) if len(self.que) else -1
