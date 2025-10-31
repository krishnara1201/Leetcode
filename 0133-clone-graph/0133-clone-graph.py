"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtocopy = {}

        cur = node
        
        if not node:
            return 
        
        def dfs(node):
            if node in oldtocopy:
                return oldtocopy[node]
            
            oldtocopy[node] = Node(node.val)
            for n in node.neighbors:
                val = dfs(n)
                if val:
                    oldtocopy[node].neighbors.append(val)

            return oldtocopy[node]

        return dfs(node)