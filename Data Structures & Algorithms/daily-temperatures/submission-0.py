class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0] * (len(temperatures))
        stack.append(0)
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                L = stack.pop()
                res[L] = i - L
            
            stack.append(i)
        
        return res