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
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda e: e[2])

        mst_weight = 0
        uf = UnionFind(n)
        edges_built = 0

        for u, v, w in edges:

            if uf.union(u, v):
                mst_weight += w
                edges_built += 1
            
            if edges_built == n - 1:
                return mst_weight


        return -1