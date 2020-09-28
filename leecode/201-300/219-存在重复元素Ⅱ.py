class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        num_dict = {}
        for i in range(n):
            if nums[i] in num_dict and i-num_dict[nums[i]]<=k:
                return True
            num_dict[nums[i]] = i
        return False
