class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) //2
            if nums[mid] == target:
                return mid
            #check if normal order
            if nums[mid] > nums[r]:
                if  nums[r] < target < nums[mid]:
                    r = mid - 1 #left segment
                else:
                    l = mid + 1 #right segment
            else:
                if  nums[mid] < target <= nums[r]:
                    l = mid + 1 #right segment
                else:
                    r = mid - 1#right segment
        return -1
                    