class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        window, ans = [], []
        for index, value in enumerate(nums):
            if index >= k and window[0] <= index-k:
                window.pop(0)
            while window and nums[window[-1]] < value:
                window.pop()
            window.append(index)
            if index >= k-1:
                ans.append(nums[window[0]])
        return ans
