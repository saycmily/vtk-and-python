class Solution:
    def canJump(self, nums) -> bool:
        # 从后往前
        # lastPos = len(nums) - 1
        # i = lastPos
        # while i >= 0:
        #     if i + nums[i] >= lastPos:
        #         lastPos = i
        #     i -= 1
        # return lastPos == 0
        # 从前往后
        m = 0
        for i in range(len(nums)):
            if i > m:
                return False
            m = max(m, i+nums[i])
        return True
