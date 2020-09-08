class Solution:
    def topKFrequent(self, nums, k: int):
        count = dict()
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        cou = sorted(count.items(), key=lambda x: x[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(cou[i][0])
        return ans
