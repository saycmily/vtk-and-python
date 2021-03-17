class Solution {
public:
    int numDistinct(string s, string t) {
        int lens = s.length(), lent = t.length();
        vector<vector<long long>> dp(lens+1, vector<long long>(lent+1, 0));
        for (int i = 0; i < lens; ++i)
            dp[i][0] = 1;
        for (int i = 0; i < lens; ++i)
            for(int j = 0; j < lent; ++j)
                if (s[i] == t[j])
                    dp[i+1][j+1] = dp[i][j] + dp[i][j+1];
                else
                    dp[i+1][j+1] = dp[i][j+1];
        return dp[lens][lent];
    }
};