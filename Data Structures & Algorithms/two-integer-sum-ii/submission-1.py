class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        while L < R:
            sum = numbers[L] + numbers[R]
            if sum == target:
                return [L + 1, R + 1]
            
            if target > sum:
                L += 1
            else:
                R -= 1

        return None