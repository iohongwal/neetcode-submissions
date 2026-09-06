class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> remains = new HashMap();
        
        for (int i = 0; i < nums.length; i++){
            int num = nums[i];
            int remain = target - num;
            if (remains.containsKey(remain)){
                return new int[] {remains.get(remain), i};
            }
            remains.put(num, i);
        }
        return null;
    }
}
