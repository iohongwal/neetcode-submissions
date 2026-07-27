class TimeMap:

    def __init__(self):
        self.arr = {}
        self.key = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.arr[(key, timestamp)] = value
        if key not in self.key:
            self.key[key] = []
        self.key[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        keyArr = self.key.get(key, [])
        l, r = 0, len(keyArr) - 1
        res = ""
        while l <= r:
            m = (l + r) //2
            if keyArr[m] <= timestamp:
                res = self.arr[(key, keyArr[m])]
                l = m + 1
            else:
                r = m - 1

        return res
        
