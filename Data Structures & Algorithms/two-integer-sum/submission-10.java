class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> remains = new HashMap();
        
        for (int i = 0; i < nums.length; i++){
            int remain = target - nums[i];
            if (remains.containsKey(remain)){
                return new int[] {remains.get(remain), i};
            }
            remains.put(nums[i], i);
        }
        return new int[]{};
    }
}
