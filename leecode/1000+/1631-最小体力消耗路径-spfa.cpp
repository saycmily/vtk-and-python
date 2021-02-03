class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int n = heights.size(), m = heights[0].size();
        vector<vector<int>> f(n, vector<int>(m, INT_MAX));
        int dx[4] = {0, 1, 0, -1}, dy[4] = {1, 0, -1, 0};

        f[0][0] = 0;
        queue<int> q;
        q.push(0);
        while(!q.empty()) {
            auto t = q.front();
            q.pop();
            int x = t / m;
            int y = t % m;

            for (int d = 0; d < 4; d++) {
                int a = x + dx[d], b = y + dy[d];
                if (a >= 0 && a < n && b >= 0 && b < m) {
                    int tmp = max(f[x][y], abs(heights[a][b] - heights[x][y]));
                    if (tmp >= f[a][b]) continue;
                    f[a][b] = tmp;
                    q.push(a*m + b);
                }
            }
        }
        return f[n-1][m-1];
    }
};