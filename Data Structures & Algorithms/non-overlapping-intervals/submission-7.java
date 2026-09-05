class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (interval1, interval2) -> Integer.compare(interval1[0], interval2[0]));
        int [] last_interval = intervals[0];
        int count = 0;
        for (int i = 1; i < intervals.length; i++){
            if (intervals[i][0] >= last_interval[1]){
                last_interval = intervals[i];
            } else {
                count++;
                if (intervals[i][1] < last_interval[1]) {
                    last_interval = intervals[i];
                }
            }

        }
        return count;
    }
}
