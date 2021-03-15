class Solution:
    def maxSubArray(self, nums) -> int:
        # res = nums[0]
        # sum = 0
        # for num in nums:
        #     if sum > 0:
        #         sum += num
        #     else:
        #         sum = num
        #     res = max(res, sum)
        # return res
        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)
