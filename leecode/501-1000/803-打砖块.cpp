struct unionfind {
    vector<int> f;
    vector<int> s;
    unionfind(int size) {
        f.resize(size);
        s.resize(size);
        for (int i = 0; i < size; ++i) {
            f[i] = i;
            s[i] = 1;
        }
    }
    int find(int x) {
        if (x == f[x]) return x;
        return f[x] = find(f[x]);
    }
    void Union(int a, int b) {
        int p = find(a), q = find(b);
        if (p == q) return;
        f[p] = q;
        s[q] += s[p];
    }
    int get_size(int x) {
        return s[find(x)];
    }
};
class Solution {
public:
    int m, n, l;
    int index(int row, int col) {
        return row * n + col;
    }
    bool IsValid(int row, int col) {
        return !(row < 0 || row > m - 1 || col < 0 || col > n - 1);
    }
    vector<int> hitBricks(vector<vector<int>>& grid, vector<vector<int>>& hits) {
        vector<vector<int>> direction = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        m = grid.size();
        n = grid[0].size();
        l = hits.size();
        vector<int> ret(l);
        vector<vector<int>> copy = grid;
        const int roof = m * n;
        unionfind uf(roof + 1);

        for (auto& hit: hits)
            copy[hit[0]][hit[1]] = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (copy[i][j] == 0) continue;
                if (i == 0) {
                    uf.Union(j, roof);
                    continue;
                }
                if (copy[i - 1][j] == 1)
                    uf.Union(index(i - 1, j), index(i, j));
                if (j > 0 && copy[i][j - 1] == 1)
                    uf.Union(index(i, j - 1), index(i, j));
            }
        }

        for(int h = l - 1; h >= 0; --h){
            int x = hits[h][0];
            int y = hits[h][1];
            if (grid[x][y] == 0) continue;
            int oldRoofSize = uf.get_size(roof);

            if (x == 0)
                uf.Union(y, roof);
            for (auto& dir: direction) {
                int newX = x + dir[0];
                int newY = y + dir[1];
                if(IsValid(newX, newY) && copy[newX][newY] == 1)
                    uf.Union(index(x, y), index(newX, newY));
            }
            int newRoofSize = uf.get_size(roof);
            ret[h] = newRoofSize - oldRoofSize - 1;
            ret[h] = ret[h] >= 0 ? ret[h] : 0;
            copy[x][y] = 1;
        }
        return ret;
    }
};