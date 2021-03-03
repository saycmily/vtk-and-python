class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> ans(num + 1, 0);
        for (int i = 1; i <= num; ++i)
            //ans[i] = ans[i&(i-1)] + 1;
            ans[i] = ans[i >> 1] + (i & 1);
        return ans;
    }
};