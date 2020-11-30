class Solution:
    def largestPerimeter(self, A: list[int]) -> int:
        nums = sorted(A, reverse = True)
        for i in range(len(nums)-2):
            su = nums[i+1] + nums[i+2]
            if nums[i] < su:
                return nums[i] + su
        return 0
