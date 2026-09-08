class Solution {
    
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] dp = new boolean[s.length() + 1];
        dp[s.length()] = true; //default status with out of the String s

        for(int i = s.length() - 1; i >= 0; i--){
            for(String word : wordDict){
                int wordLen = word.length();
                if (i + wordLen <= s.length() && word.equals(s.substring(i, i + wordLen)))
                    dp[i] = dp[i + wordLen];
                //Once the subString can be found in the wordDict, break the loop
                if (dp[i]) break;
            }
        }

        return dp[0];
    }
}
