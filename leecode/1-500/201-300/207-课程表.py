class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        import collections
        # 存储有向图
        edges = collections.defaultdict(list)
        # 存储每个节点的入度
        indeg = [0] * numCourses
        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1
        # 将所有入度为 0 的节点放入队列中
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        while q:
            # 从队首取出一个节点
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        for i in indeg:
            if i > 0:
                return False
        return True
