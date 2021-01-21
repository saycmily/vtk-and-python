class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        if (strs.size() == 0) return 0;
        int dp[m+1][n+1];
        for (int i = 0; i <= m; ++i)
            for (int j = 0; j <= n; ++j)
                dp[i][j] = 0;
        for (auto& str : strs) {
            int zero = 0, one = 0;
            for (auto& s : str) {
                if (s == '1')
                    one += 1;
                else
                    zero += 1;
            }
            for (int i = m; i >= zero; --i)
                for (int j = n; j >= one; --j)
                    dp[i][j] = max(dp[i][j], 1+dp[i-zero][j-one]);
        }
        return dp[m][n];
    }
};