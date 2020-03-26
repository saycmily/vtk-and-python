class Solution:
    def largestRectangleArea(self, heights):
        stack = [-1]
        maxarea = 0
        for i in range(len(heights)):
            while len(stack) > 1 and heights[i] <= heights[stack[-1]]:
                maxarea = max(maxarea, heights[stack.pop()] * (i-stack[-1]-1))
            stack.append(i)
        # for i in range(len(stack)-1):
        while stack[-1] != -1:
            maxarea = max(maxarea, heights[stack.pop()] * (len(heights)-stack[-1]-1))
        return maxarea

    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        maxarea = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0  # else 0 精髓
            maxarea = max(maxarea, self.largestRectangleArea(dp))
        return maxarea
