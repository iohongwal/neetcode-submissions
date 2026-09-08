class Solution {
    public int maxProduct(int[] nums) {
        int curMax = nums[0], curMin = nums[0], res = nums[0];
        for(int i = 1; i < nums.length; i++){
            int tempMax = curMax;
            curMax = Math.max(nums[i], Math.max(tempMax*nums[i], curMin*nums[i]));
            curMin = Math.min(nums[i], Math.min(tempMax*nums[i], curMin*nums[i]));
            res = Math.max(curMax, res);
        }
        return res;
    }
}
