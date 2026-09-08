class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l = 0;
        int maxLen = 0;
        Set<Character> substring = new HashSet<>(); 
        for (int r = 0; r < s.length(); r++){
            while (substring.contains(s.charAt(r))){
                substring.remove(s.charAt(l));
                l++;
            }
            substring.add(s.charAt(r));
            maxLen = Math.max(maxLen, substring.size());
        }

        return maxLen;
    }
}
