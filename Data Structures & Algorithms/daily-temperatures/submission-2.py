class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = deque()
        stack.append(0)
        for r in range(1, len(temperatures)):
            while (
                stack and 
                temperatures[r] >  temperatures[stack[-1]]
                ):
                l = stack.pop()
                res[l] = r - l
            
            stack.append(r)
        
        return res
