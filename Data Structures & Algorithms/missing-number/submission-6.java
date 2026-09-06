class Solution {
    public int missingNumber(int[] nums) {
        int missing_num = nums.length;
        for (int i = 0; i < nums.length; i++){
            missing_num += i;
            missing_num -= nums[i];
        }
        return missing_num;
    }
}
