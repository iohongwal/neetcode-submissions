class Solution {
    public int countComponents(int n, int[][] edges) {
        int res = 0;
        HashMap<Integer, List<Integer>> adjHash = new HashMap<>();
        Set<Integer> visited = new HashSet<>();
        for (int[] edge: edges) {
            adjHash.computeIfAbsent(edge[0], k -> new ArrayList<>()).add(edge[1]);
            adjHash.computeIfAbsent(edge[1], k -> new ArrayList<>()).add(edge[0]);
        }


        for (int i = 0; i < n; i++){

            if (visited.contains(i)){
                continue;
            }
            res ++;
            Deque<Integer> stack = new ArrayDeque<>();
            stack.push(i);
            while (!stack.isEmpty()){
                int n1 = stack.pop();
                if (visited.contains(n1)) continue;
                visited.add(n1);
                if (!adjHash.containsKey(n1)){
                    continue;
                }
                for (int n2: adjHash.get(n1)){
                    stack.push(n2);
                }
            }
        }

        return res;
    }
}
