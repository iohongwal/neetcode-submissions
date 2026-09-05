class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (interval1, interval2) -> Integer.compare(interval1[0], interval2[0]));
        int last_end = intervals[0][1];
        int count = 0;
        for (int i = 1; i < intervals.length; i++){
            //check the start time is further than last end time
            if (intervals[i][0] >= last_end){
                last_end = intervals[i][1];
            } else {
                count++;
                if (intervals[i][1] < last_end) {
                    last_end = intervals[i][1];
                }
            }

        }
        return count;
    }
}
