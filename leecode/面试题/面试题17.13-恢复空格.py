class Solution:
    def respace(self, dictionary, sentence: str) -> int:
        dp = [0]*(len(sentence)+1)

        for i in range(len(sentence)+1):
            if i == 0:
                temp_num = 0
            else:
                temp_num = dp[i-1]+1
            for j in range(i-1, -1, -1):
                if sentence[j:i] in dictionary:
                    temp_num = min(temp_num, dp[j])
            dp[i] = temp_num
        return dp[-1]
