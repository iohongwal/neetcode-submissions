class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // java's built in heap;
        Map<Integer, Integer> map = new HashMap();
        for (int x : nums) map.put(x, map.getOrDefault(x, 0)+1);
        PriorityQueue<Integer> heap = new PriorityQueue<>(
            (a,b) -> Integer.compare(map.get(a), map.get(b)));
        int size = 0;
        for(int key : map.keySet()) {
            heap.offer(key);
            if(heap.size()>k) heap.poll();
        }
        
        int res[] = new int[k];
        for (int i= 0; i<k; i++) {
            res[i] = heap.poll();
        }
        return res;

    }
}
