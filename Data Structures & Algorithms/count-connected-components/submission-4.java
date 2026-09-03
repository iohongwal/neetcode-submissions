class Solution {
    public int countComponents(int n, int[][] edges) {
        //method with DFS and ArrayList<ArrayList<Integer>>
        ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();
        
        //inital the adjList
        for (int i = 0; i < n; i++){
            //inital arrayList into adjList[i]
            adjList.add(new ArrayList<>());   
        }

        //create the adjList with node and its neigbhor
        for(int[] edge: edges){
            //bidirectional
            adjList.get(edge[0]).add(edge[1]);
            adjList.get(edge[1]).add(edge[0]);
        }

        int[] visited = new int[n];
        int count = 0;

        //loop through each node
        for (int i = 0; i < n; i++){
            if (visited[i] == 0){
                count++;
                dfs(i, adjList, visited);
            }
        }

        return count;
    }

    private void dfs(int i, ArrayList<ArrayList<Integer>> adjList, int[] visited){
        visited[i] = 1;
        for (int node: adjList.get(i)){
            if (visited[node] == 0) dfs(node, adjList, visited);
        }
    }
    
}
