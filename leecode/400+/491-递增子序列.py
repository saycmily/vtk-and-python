class Solution:
    def findSubsequences(self, nums):
        ans = set()

        def dfs(step, track):
            if step > len(nums):
                return
            if len(track) >= 2:
                if track[-1] < track[-2]:
                    return
                temp = tuple(track)
                if temp not in ans:
                    ans.add(temp)
            for i in range(step, len(nums)):
                track.append(nums[i])
                dfs(i+1, track)
                track.pop()
        dfs(0, [])
        return list(ans)
