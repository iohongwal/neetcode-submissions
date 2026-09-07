class Solution {
    public int climbStairs(int n) {
        if(n == 0 || n == 1) return 1;
        int[] steps = new int[n + 1];
        steps[0] = 1;
        steps[1] = 1;
        for (int i = 2; i <= n; i++){
            //1 steps before to current steps + 2 steps before to current steps
            steps[i] = steps[i - 1] + steps[i - 2];
        }
        return steps[n];
    }
}
