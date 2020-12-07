class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        count = [0] * 26
        for i in tasks:
            x = ord(i) - ord('A')
            count[x] += 1
        count.sort()
        maxcount = 0
        for i in range(25, -1, -1):
            if count[i] != count[25]:
                break
            maxcount += 1
        ans = (count[25]-1)*(n+1) + maxcount
        return max(ans, len(tasks))
