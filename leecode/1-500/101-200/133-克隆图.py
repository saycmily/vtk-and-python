# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node):
            if node not in had:
                had[node] = new = Node(node.val, None)
                new.neighbors = [*map(dfs, node.neighbors)]
            return had[node]
        if not node:
            return None
        had = dict()
        return dfs(node)
