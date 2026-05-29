class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def graphDFS(image, sr, sc, color, originalColor):
            ROW, COL = len(image), len(image[0])
            if (sr >= ROW or sc >= COL or min(sr, sc) < 0 #check out of bound
                or image[sr][sc] != originalColor #Check if it is same as originalColor
                or image[sr][sc] == color
                ):
                return
            
            image[sr][sc] = color

            graphDFS(image, sr + 1, sc, color, originalColor)
            graphDFS(image, sr - 1, sc, color, originalColor)
            graphDFS(image, sr, sc + 1, color, originalColor)
            graphDFS(image, sr, sc - 1, color, originalColor)
            
        graphDFS(image, sr, sc, color, image[sr][sc])
        return image


