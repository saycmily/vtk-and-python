def largestRectangleArea(self, heights):
    # res = 0
    # n = len(heights)
    # for i in range(n):
    #     res = max(res,heights[i])
    #     h_min = heights[i]
    #     for j in range(i+1,n):
    #         h_min = min(h_min, heights[j])
    #         res = max(res, h_min*(j-i+1))
    # return res
    stack = [-1]
    max_res = 0
    for i in range(len(heights)):
        while len(stack) > 1 and heights[i] <= heights[stack[-1]]:
            # stack.pop()不能分开写 可能会遇到栈第一个元素-1
            max_res = max(max_res, heights[stack.pop()] * (i - stack[-1] - 1))
        stack.append(i)
    for i in range(len(stack)-1):
        max_res = max(max_res, heights[stack.pop()]*(len(heights)-1-stack[-1]))
    return max_res
