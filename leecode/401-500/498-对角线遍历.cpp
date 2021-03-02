class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if (m == 0) return {};
        int n = matrix[0].size();
        vector<int> ans;
        bool flag = false;
        for (int i = 0; i < n; ++i) {
            int x = 0, y = i;
            vector<int> cur;
            while (y >= 0 && x < m) {
                cur.emplace_back(matrix[x][y]);
                x ++;
                y --;
            }
            if (!flag)
                reverse(cur.begin(), cur.end());
            flag = !flag;
            ans.insert(ans.end(), cur.begin(), cur.end());
        }
        for (int i = 1; i < m; ++i) {
            int x = i, y = n-1;
            vector<int> cur;
            while (x < m && y >= 0) {
                cur.emplace_back(matrix[x][y]);
                x ++;
                y --;
            }
            if (!flag)
                reverse(cur.begin(), cur.end());
            flag = !flag;
            ans.insert(ans.end(), cur.begin(), cur.end());
        }
        return ans;
    }
};