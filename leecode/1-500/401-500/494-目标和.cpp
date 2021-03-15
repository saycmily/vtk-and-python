class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int sum = 0;
        for (int n : nums) sum += n;
        if (sum < S || (sum + S) % 2 == 1) return 0;
        int t = (S + sum) / 2;
        vector<int> dp(t+1, 0);
        dp[0] = 1;
        for (int num : nums)
            for (int j = t; j >= num; j--)
                dp[j] += dp[j - num];
        return dp[t];
    }
};