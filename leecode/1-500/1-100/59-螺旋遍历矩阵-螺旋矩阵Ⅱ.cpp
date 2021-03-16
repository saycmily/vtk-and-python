class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> ans(n, vector<int>(n, 0));
        int ind = 0, cur = 1;
        while (ind < n/2) {
            for (int i = ind; i < n-ind; ++i) {
                ans[ind][i] = cur;                
                cur ++;
            }
            for (int j = ind+1; j < n-1-ind; ++j) {
                ans[j][n-1-ind] = cur;
                cur ++;
            }
            for (int k = n-1-ind; k >= ind; --k) {
                ans[n-1-ind][k] = cur;
                cur ++;
            }
            for (int z = n-2-ind; z >= ind+1; --z) {
                ans[z][ind] = cur;
                cur ++;
            }
            ind ++;
        }
        if (n % 2)
            ans[n/2][n/2] = cur;
        return ans;
    } 
};