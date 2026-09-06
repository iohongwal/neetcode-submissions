class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> numCount = new HashMap();
        int mostFreq = 0;
        //iterate the array to count the frequency for each element
        for (int num : nums) numCount.put(num, numCount.getOrDefault(num, 0) + 1);

        List<Integer>[] numFreq = new List[nums.length + 1];
        //initial the numFreq and add num:count to numFreq
        for (int num : numCount.keySet()){
            int freq = numCount.get(num);
            if (numFreq[freq] == null) numFreq[freq] = new ArrayList<>();
            numFreq[freq].add(num);
        } 

        int[] res = new int[k];
        int idx = 0;
        for (int i = numFreq.length - 1; i >= 0 && idx < k; i--){
            if (numFreq[i] == null) continue;
            for (int num : numFreq[i]){
                res[idx++] = num;
                if (idx == k) return res;
            }
        }
        return res;
    }
}
