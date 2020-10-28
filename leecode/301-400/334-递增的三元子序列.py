class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        length = len(nums)
        if length < 3:
            return False
        
        min_num = float('inf')
        max_num = float('inf')
        
        for n in nums:
            if n < min_num:
                min_num = n
            elif min_num < n and n <= max_num:
                max_num = n
            elif n > max_num:
                return True
        
        return False
