class UnionFind:

    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, n: int) -> int:
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, n1: int, n2: int) -> bool:
        root_n1, root_n2 = self.find(n1), self.find(n2)
        if root_n1 == root_n2:
            return False
        
        if self.rank[root_n1] > self.rank[root_n2]:
            self.parent[root_n2] = root_n1
            self.rank[root_n1] += self.rank[root_n2] 
        else:
            self.parent[root_n1] = root_n2
            self.rank[root_n2] += self.rank[root_n1] 

        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i) #[n1, n2, weight, original_index]
        
        edges.sort(key = lambda e: e[2])
        
        uf = UnionFind(n)
        mst_weight = 0

        #find the minimun spanning tree
        for n1, n2, w, i in edges:
            if uf.union(n1, n2):
                mst_weight += w
                
        critical, pseudo = [],[] #critical and pseudo-critical edges

        for n1, n2, e_weight, i in edges:
            #Try without the edges (critical edge)
            weight = 0
            uf = UnionFind(n)
            for v1, v2, w, j in edges:
                if i != j and uf.union(v1, v2):
                    weight += w
            #The edges delection cause the MST weight increase is called a critical edge
            #And check if it is the MST
            if max(uf.rank) != n or weight > mst_weight:
                critical.append(i)
                continue

            #Try with the edges (pseudo-critical edges)
            uf = UnionFind(n)
            uf.union(n1, n2)
            weight = e_weight
            for v1, v2, w, j in edges:
                if uf.union(v1, v2):
                    weight += w
            if weight == mst_weight:
                pseudo.append(i)

        return [critical, pseudo]


            

