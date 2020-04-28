class Solution:
    def findContinuousSequence(self, target: int):
        def backtrack(i, target, nums):
            if i + 1 == target:
                nums.append(i+1)
                res.append(nums[:])
            elif i + 1 > target:
                return
            else:
                nums.append(i+1)
                target -= i + 1
                backtrack(i + 1, target, nums)

        res = []
        x = target
        for i in range(1, target):
            nums = []
            nums.append(i)
            target -= i
            backtrack(i, target, nums)
            target = x

        return res
