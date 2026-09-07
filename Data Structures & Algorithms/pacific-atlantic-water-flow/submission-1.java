class Solution {
    //initialize four direction
    int[][] neighbors = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        //initialize two boolean[][] to store the point that reach by the flow from each Ocean
        boolean[][] pacifics = new boolean[heights.length][heights[0].length];
        boolean[][] atlantics  = new boolean[heights.length][heights[0].length];

        //iterate top and left side for Pacific Ocean 
        for (int r = 0; r < heights.length; r++){
            dfs(r, 0, 0, heights, pacifics);
        }
        for (int c = 0; c < heights[0].length; c++){
            dfs(0, c, 0, heights, pacifics);
        }
            
        //iterate bottom and right side for Atlantic Ocean 
        for (int r = 0; r < heights.length; r++){
            dfs(r, heights[0].length - 1, 0, heights, atlantics);
        }
        for (int c = 0; c < heights[0].length; c++){
            dfs(heights.length - 1, c, 0, heights, atlantics);
        }

        List<List<Integer>> overlap = new ArrayList<>();
        //Check any cells that both flow from Pacific and Atlantic oceans
        for (int r = 0; r < heights.length; r++){
            for (int c = 0; c < heights[0].length; c++){
                if (pacifics[r][c] && atlantics[r][c]){
                    overlap.add(List.of(r, c));
                }
            }
        }
        
        return overlap;
    }

    void dfs(int r, int c, int lastHeight, int[][]heights, boolean[][] visited){
        if (r >= heights.length || c >= heights[0].length 
            || r < 0 || c < 0 || visited[r][c] 
            || heights[r][c] < lastHeight){
                return;
        }
            

        visited[r][c] = true;
        for (int[] neighbor: neighbors){
            int newR = r + neighbor[0];
            int newC = c + neighbor[1];
            dfs(newR, newC, heights[r][c], heights, visited);
        }
    }
}
