class TimeMap:

    def __init__(self):
        self.arr = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.arr[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        for t in range(timestamp, -1, -1):
            if (key, t) in self.arr:
                return self.arr[(key, t)]
        
        return ""
        
