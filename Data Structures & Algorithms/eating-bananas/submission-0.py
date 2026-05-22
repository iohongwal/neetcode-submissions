import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        min_mid = high
        while low <= high:
            hours = 0
            mid = (low + high) // 2
            for pile in piles:
                hours += math.ceil(pile / mid)
            if h >= hours:
                high = mid - 1
                min_mid = mid
            elif h < hours:
                low = mid + 1
        return min_mid