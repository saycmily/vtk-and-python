class Solution:
    def verifyPostorder(self, postorder) -> bool:
        def helper(nums):
            if len(nums) <= 1:
                return True
            root = nums[-1]
            for i in range(len(nums)):
                if nums[i] > root:
                    break
            for j in range(i, len(nums)-1):
                if nums[j] < root:
                    return False
            return helper(nums[:i]) and helper(nums[i:-1])

        if not postorder:
            return True
        return helper(postorder)
