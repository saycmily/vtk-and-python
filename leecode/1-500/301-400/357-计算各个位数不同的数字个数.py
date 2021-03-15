class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 10
        for i in range(2, n+1):
            # dp[i-1]-dp[i-2]的意思是我们上一次较上上一次多出来的各位不重复的数字。
            # 以n=3为例，n=2已经计算了0-99之间不重复的数字了，我们需要判断的是100-999之间不重复的数字，那也就只能用10-99之间的不重复的数去组成三位数，而不能使用0-9之间的不重复的数，因为他们也组成不了3位数。而10-99之间不重复的数等于dp[2]-dp[1],(11-i)表示还剩多少可选择数字
            dp[i] = dp[i-1] + (dp[i-1]-dp[i-2]) * (11-i)
        return dp[n]
