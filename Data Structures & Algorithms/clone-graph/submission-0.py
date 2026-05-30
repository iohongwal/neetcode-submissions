"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        adjList = {}
        def graphDFS(curNode):
            if curNode in adjList:
                return adjList[curNode]
            
            copy = Node(curNode.val)
            adjList[curNode] = copy
            for nextNode in curNode.neighbors:
                copy.neighbors.append(graphDFS(nextNode))
            return copy

        return graphDFS(node) if node else None
            