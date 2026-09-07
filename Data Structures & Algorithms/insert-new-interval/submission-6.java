class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();
        for (int[] interval : intervals){
            /*
            Noted that the given intervals is sorted in ascending order

            Compare the current interval end and new interval start time.
            If the new interval start time is smaller or equal than the current interval end time, 
            it means these two interval is overlapped, thus these two interval will be merge.

            */
            if (interval[1] < newInterval[0]){
                result.add(interval);
            } else if (interval[0] > newInterval[1]){
                result.add(newInterval);
                newInterval = interval;
            }else{
                newInterval[0] = Math.min(interval[0], newInterval[0]);
                newInterval[1] = Math.max(interval[1], newInterval[1]);
            }
        }
        result.add(newInterval);
        return result.toArray(new int[result.size()][]);
    }
}