class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        HashMap<Character, Integer> letter_count = new HashMap<>();
        for (char c: s.toCharArray()){
            if (letter_count.containsKey(c))
                letter_count.put(c, letter_count.get(c) + 1);
            else
                letter_count.put(c, 1);
        }

        for (char c: t.toCharArray()){
            if (!letter_count.containsKey(c) || letter_count.get(c) == 0)
                return false;
            else
                letter_count.put(c, letter_count.get(c) - 1);
        }

        return true;
    }
}
