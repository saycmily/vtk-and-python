class Solution:
    def findCircleNum(self, isConnected) -> int:
        from collections import deque
        n = len(isConnected)
        all_city = set(range(n))

        def dfs(city, all_city):
            q = deque([city])
            while q:
                ci = q.pop()
                for i in range(n):
                    if i in all_city and isConnected[ci][i] == 1:
                        q.append(i)
                        all_city.remove(i)
            return all_city

        ans = 0
        while all_city:
            city = all_city.pop()
            all_city = dfs(city, all_city)
            ans += 1
        return ans
