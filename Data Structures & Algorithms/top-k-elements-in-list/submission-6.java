class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> numCount = new HashMap();
        int mostFreq = 0;
        //iterate the array to count the frequency for each element
        for (int num : nums){
            if (numCount.containsKey(num))
                numCount.put(num, numCount.get(num) + 1);
            else
                numCount.put(num, 1);
            mostFreq = Math.max(mostFreq, numCount.get(num));
        }
        
        List<List<Integer>> numFreq = new ArrayList<>();
        //initial the numFreq
        for (int i = 0; i <= mostFreq; i++){
            numFreq.add(new ArrayList<Integer>());
        }

        //add num:count to numFreq
        for (int num : numCount.keySet()){
            numFreq.get(numCount.get(num)).add(num);
        } 

        int[] res = new int[k];
        int j = 0;
        for (int i = mostFreq; i > 0; i--){
            for (int num : numFreq.get(i)){
                res[j++] = num;
                if (j >= k) return res;
            }
        }
        return res;
    }
}
