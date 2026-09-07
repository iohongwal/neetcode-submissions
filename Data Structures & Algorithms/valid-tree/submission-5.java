class Solution {
    //initialize adjList from 0 to n - 1
    List<List<Integer>> adjList = new ArrayList<>();
    Set<Integer> visited = new HashSet<>();

    public boolean validTree(int n, int[][] edges) {
        for (int i = 0; i < n; i++){
            adjList.add(new ArrayList<>());
        }
        //initialize adjList for each node and its neighbor
        for (int[] edge : edges){
            //undirected edges 
            adjList.get(edge[0]).add(edge[1]);
            adjList.get(edge[1]).add(edge[0]);
        }

        //return the result for dfs method and check if all nodes are visited
        //As there are no prev node for node 0, we use -1
        return dfsTree(0, -1) && visited.size() == n;
    }

    boolean dfsTree(int node, int prev_node){
        //Check if node have already visited in previously
        if (visited.contains(node)) return false;

        //add the node into visited as a record to detect loop
        visited.add(node);

        //iterate each its neighbor
        for (int neighbor : adjList.get(node)){
            /*
                As the edge is undirected, thus if the edge is connected its previous node,
                it won't consider as a loop.
            */
            if (neighbor == prev_node){ 
                continue;
            }else{
                //check if its neighbor contains any loop, if it does contain loop return false
                if (!dfsTree(neighbor, node)) return false; 
            }
        }

        return true;
    }
}
