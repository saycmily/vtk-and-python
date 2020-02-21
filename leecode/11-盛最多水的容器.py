# 双指针  短的向中间移动
def maxArea(height):
    i = 0
    j = len(height) - 1
    ans = 0
    while i != j:
        ans = max(ans, min(height[i], height[j])*(j-i))
        if height[i] <= height[j]:
            i += 1
        else:
            j -= 1
    return ans
