class Solution {
    public int coinChange(int[] coins, int amount) {
        
        int[] changes = new int[amount + 1];
        Arrays.fill(changes, amount + 1);
        changes[0] = 0;
        //iterate each coin to check the min coins change for amount 0 to given amount 
        for (int coin: coins){
            for (int i = 0; i <= amount; i++){
                if (i >= coin){
                    changes[i] =  Math.min(changes[i], 1 + changes[i - coin]);
                }
            }
        }

        return (changes[amount] != amount + 1) ? changes[amount] : -1;
    }
}
