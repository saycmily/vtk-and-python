class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        for (int i = 0; i < n; ++i) {
            int x = 1, y = i+1;
            int standard = matrix[0][i];
            while (x < m && y < n) {
                if (matrix[x][y] != standard)
                    return false;
                x ++; y++;
            }
        }
        for (int j = 1; j < m; ++j) {
            int x = j+1, y = 1;
            int standard = matrix[j][0];
            while (x < m && y < n) {
                if (matrix[x][y] != standard)
                    return false;
                x ++; y ++;
            }
        }
        return true;
    }
};