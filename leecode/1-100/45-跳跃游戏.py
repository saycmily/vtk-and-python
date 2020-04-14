def jump(self, nums):
    steps = 0
    end = 0
    maxposition = 0
    for i in range(len(nums) - 1):
        maxposition = max(maxposition, nums[i] + i)
        if i == end:
            end = maxposition
            steps += 1
    return steps
