class Solution {
public:
    int minCut(string s) {
        int n = s.length();
        vector<int> dp(n+1, n);
        dp[0] = -1;
        for (int i = 0; i < n; ++i) 
            for (int j = 0; j < i+1; ++j) 
                if (isHuiwen(s, j, i))
                    dp[i+1] = min(dp[i+1], dp[j] + 1);
        return dp[n];

    }
    //判断回文串
    bool isHuiwen(string s, int start, int end) {
        int i = start, j = end;
        while(i < j) {
            if(s[i] != s[j]) 
                return false;
            i++; j--;
        }
        return true;
    }
};