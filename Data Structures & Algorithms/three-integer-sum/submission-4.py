class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, z = i + 1, len(nums) - 1
            
            while j < z:
                total = nums[i] + nums[j] + nums[z]
                if total < 0:
                    j += 1
                elif total > 0:
                    z -= 1
                else:
                    res.append([nums[i], nums[j], nums[z]])
                    j += 1
                    z -= 1

                    while j < z and nums[j] == nums[j - 1]:
                        j += 1

        return res
