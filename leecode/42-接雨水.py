def trap(height):
    ans = 0
    h1 = 0
    h2 = 0
    for i in range(len(height)):
        h1 = max(h1, height[i])
        h2 = max(h2, height[-i-1])
        ans = ans + h1 + h2 - height[i]
    return ans - len(height)*h1


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))
