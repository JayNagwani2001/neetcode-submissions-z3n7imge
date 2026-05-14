"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         if node is None:
#             return None

#         n = Node(node.val)
#         vis = set()

#         def dfs(node, n, par):
#             if node.val in vis:
#                 return

#             vis.add(node.val)

#             for ch in node.neighbors:
            
#                 if ch.val in vis:
#                     if par != -1:
#                         n.neighbors.append(par)
#                     continue

#                 new = Node(ch.val)
#                 n.neighbors.append(new)
#                 dfs(ch, new, n)

#         dfs(node, n, -1)

#         return n
        
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None

        vis = {}

        def dfs(node):

            if node in vis:
                return vis[node]

            clone = Node(node.val)
            vis[node] = clone

            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone

        return dfs(node)