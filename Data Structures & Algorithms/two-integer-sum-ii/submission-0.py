class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(numbers)):
            diff =  target - numbers[i]
            if diff in nums_map:
                return [nums_map[diff], i + 1]
            
            nums_map[numbers[i]] = i + 1
            
        return None