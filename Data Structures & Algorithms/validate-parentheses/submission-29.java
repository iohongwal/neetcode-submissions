class Solution {
    public boolean isValid(String s) {

        Map<Character, Character> parenthese = new HashMap<>(
            Map.of('{','}','[',']','(',')')
        );
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()){
            if (parenthese.containsKey(c))
                stack.push(parenthese.get(c));
            else{
                if(stack.isEmpty() || c != stack.peek())
                    return false;
                stack.pop();
            }
        }
        return stack.isEmpty();
    }
}
