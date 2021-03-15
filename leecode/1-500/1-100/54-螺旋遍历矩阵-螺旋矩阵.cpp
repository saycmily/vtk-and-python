class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if (m == 0) return vector<int> {};
        int n = matrix[0].size();
        if (n == 0) return vector<int> {};
        vector<int> ans;
        for(int x : matrix[0])
            ans.emplace_back(x);
        for(int i = 1; i < m - 1; ++i)
            ans.emplace_back(matrix[i][n-1]);
        if (m > 1)
            for(int j = n-1; j >= 0; --j)
                ans.emplace_back(matrix[m-1][j]);
        if (n > 1)
            for(int k = m-2; k >= 1; --k)
                ans.emplace_back(matrix[k][0]);
        matrix.erase(matrix.begin());
        if (m > 1)
            matrix.erase(matrix.end()-1);
        for (vector<int>& ma : matrix) {
            ma.erase(ma.begin());
            if (n > 1)
                ma.erase(ma.end()-1);
        }
        vector<int> next = spiralOrder(matrix);
        ans.insert(ans.end(), next.begin(), next.end());
        return ans;
    }
};