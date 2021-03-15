class Solution:
    def frequencySort(self, s: str) -> str:
        dis = dict()
        for i in s:
            if i in dis:
                dis[i] += 1
            else:
                dis[i] = 1
        d = sorted(dis.items(), key = lambda x: x[1], reverse = True)
        ans = ""
        for i,j in d:
            ans += i*j
        return ans
