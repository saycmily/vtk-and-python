def findContinuousSequence(self, target):
    def backtrack(i, target):
        if i + 1 == target:
            nums.append(i+1)
            res.append(nums[:])
        elif i + 1 > target:
            return
        else:
            nums.append(i+1)
            target -= i + 1
            backtrack(i + 1, target)

    res = []
    x = target
    for i in range(1, target):
        nums = []
        nums.append(i)
        target -= i
        backtrack(i, target)
        target = x

    return res
