def minDistance(self, word1: str, word2: str) -> int:
    # 动态规划自底向上
    m = len(word1)
    n = len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # 第一行
    for i in range(1, n + 1):
        dp[0][i] = dp[0][i-1] + 1
    # 第一列
    for j in range(1, m + 1):
        dp[j][0] = dp[j-1][0] + 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
    return dp[-1][-1]

# 自顶向下
# import functools
# class Solution:
#     @functools.lru_cache(None)
#     def minDistance(self, word1: str, word2: str) -> int:
#         if not word1 or not word2:
#             return len(word1) + len(word2)
#         if word1[0] == word2[0]:
#             return self.minDistance(word1[1:], word2[1:])
#         else:
#             inserted = 1 + self.minDistance(word1, word2[1:])
#             deleted = 1 + self.minDistance(word1[1:], word2)
#             replace = 1 + self.minDistance(word1[1:], word2[1:])
#             return min(inserted, deleted, replace)
