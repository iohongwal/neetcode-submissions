class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adjHash = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adjHash[n1].append(n2)
        
        visited = set() #Visited nodes
        visiting = set() #Nodes being visted in the curr dfs call(used to detect cycles)
        top_sort = []

        def dfs(src):
            if src in visited:
                return True
            
            if src in visiting:
                return False
            
            visiting.add(src)

            for n in adjHash[src]:
                if not dfs(n):
                    return False
                    
            visiting.remove(src)
            visited.add(src)
            top_sort.append(src)
            return True
        
        for i in range(n):
            if not dfs(i):
                return [] # Cycle detected

        top_sort.reverse()

        return top_sort