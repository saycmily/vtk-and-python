def canJump(nums):
    lastPos = len(nums) - 1
    i = lastPos
    while i >= 0:
        if i + nums[i] >= lastPos:
            lastPos = i
        i -= 1
    return lastPos == 0
