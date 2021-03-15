class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        # 出度入度问题，用字典{s:[]} 格式存储
        from collections import defaultdict
        if not edges:
            if n == 0:
                return []
            else:
                return [i for i in range(n)]
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        leaves = [i for i in graph if len(graph[i]) == 1]
        while n > 2:
            n -= len(leaves)
            nxt = set()
            for leave in leaves:
                tmp = graph[leave].pop()
                graph[tmp].remove(leave)
                if len(graph[tmp]) == 1:
                    nxt.add(tmp)
            leaves = nxt
        return list(leaves)
