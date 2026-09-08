class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int profit = 0;
        for (int price : prices){
            profit = Math.max(profit, price - minPrice);
            minPrice = Math.min(price, minPrice);
        }
        return profit;
    }
}
