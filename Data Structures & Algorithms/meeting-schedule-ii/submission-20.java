/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        if (intervals.size() < 1) return intervals.size();

        // Sort by start time
        intervals.sort((a, b) -> Integer.compare(a.start, b.start));

        //minHeap to track the active room end time (occurring)
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for (Interval interval : intervals){
            //If the min end time <= the current meeting start time, the room is free
            if (!minHeap.isEmpty() && minHeap.peek() <= interval.start)
                minHeap.poll();

            //add the current meeting end time into minHeap
            minHeap.add(interval.end);
        }
        //return number of the remaining room
        return minHeap.size();
    }
}
