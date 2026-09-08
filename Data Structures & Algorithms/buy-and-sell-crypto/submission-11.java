class Solution {
    public int maxProfit(int[] prices) {
        int buyIdx = 0;
        int sellIdx = 1;
        int profit = 0;
        while (sellIdx < prices.length){
            profit = Math.max(profit, prices[sellIdx] - prices[buyIdx]);
            if ((prices[sellIdx] - prices[buyIdx]) < 0)
                sellIdx = ++buyIdx + 1;
            else
                sellIdx++;
        }
        return profit;
    }
}
