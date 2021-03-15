import random

class Solution:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def reset(self) -> list[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums


    def shuffle(self) -> list[int]:
        """
        Returns a random shuffling of the array.
        """
        temp = self.nums[:]
        random.shuffle(temp)
        return temp



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()