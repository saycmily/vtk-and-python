def subsetsWithDup(nums):
    n = len(nums)
    nums.sort()

    def backtrack(i=0, list_one=[]):
        res.append(list_one[:])
        for j in range(i, n):
            if j > i and nums[j] == nums[j-1]:
                continue
            list_one.append(nums[j])
            backtrack(j + 1, list_one)
            list_one.pop()
    res = []
    backtrack()
    return res
