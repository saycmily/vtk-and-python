def subsets(self, nums):
    def backtrack(first=0, curr=[], k=0):
        if len(curr) == k:
            output.append(curr[:])
            return
        for i in range(first, len(nums)):
            curr.append(nums[i])
            backtrack(i + 1, curr, k)
            curr.pop()
    output = [[]]
    if not nums:
        return output
    for i in range(1, len(nums)+1):
        backtrack(k=i)
    return output
