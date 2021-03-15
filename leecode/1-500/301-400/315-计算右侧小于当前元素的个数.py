# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         ans = []
#         for i in range(n):
#             cur = nums[i]
#             num = 0
#             for j in nums[i+1:]:
#                 if j < cur:
#                     num += 1
#             ans.append(num)
#         return ans


class Solution:
    def countSmaller(self, nums):
        import bisect
        queue = []
        res = []
        for num in nums[::-1]:
            loc = bisect.bisect_left(queue, num)
            res.append(loc)
            queue.insert(loc, num)
        return res[::-1]
