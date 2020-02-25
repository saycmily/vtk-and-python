def searchRange(self, nums, target):
    ans = []
    for index, value in enumerate(nums):
        if value == target:
            ans.append(index)
            ans.append(index + nums.count(value) - 1)
            return ans
        elif value > target:
            return [-1, -1]
    return [-1, -1]
