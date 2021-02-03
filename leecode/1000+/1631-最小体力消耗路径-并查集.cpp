struct UnionFind {
    vector<int> fa;
    UnionFind(int n) {
        fa.resize(n);
        for(int i = 0; i < n; i++)
            fa[i] = i;
    }
    int Find(int i) {
        return fa[i] == i ? i : (fa[i] = Find(fa[i]));
    }
    void Union(int i, int j) {
        int rooti = Find(i);
        int rootj = Find(j);
        fa[rooti] = rootj;
    }
};

class Solution {
public:
    int m, n;
    int GetIndex(int row, int col) {
        return row * n + col;
    }
    bool IsValid(int row, int col) {
        return row >= 0 && row < m && col >= 0 && col < n;
    }
    int minimumEffortPath(vector<vector<int>>& heights) {
        m = heights.size();
        n = heights[0].size();
        int topleft = GetIndex(0, 0);
        int bottomright = GetIndex(m - 1, n - 1);

        UnionFind uf(m * n);

        // key为高度差，value为格子与上格子/左格子之间高度差与key相等的index列表。
        map<int, vector<pair<int, int> > > dist;

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(i > 0) {
                    int h = abs(heights[i][j] - heights[i - 1][j]);
                    if(dist.find(h) == dist.end()) {
                        vector<pair<int, int> > v;
                        dist.insert(make_pair(h, v));
                    }
                    dist[h].push_back(make_pair(GetIndex(i, j), GetIndex(i - 1, j)));
                }
                if(j > 0) {
                    int h = abs(heights[i][j] - heights[i][j - 1]);
                    if(dist.find(h) == dist.end()) {
                        vector<pair<int, int> > v;
                        dist.insert(make_pair(h, v));
                    }
                    dist[h].push_back(make_pair(GetIndex(i, j), GetIndex(i, j - 1)));
                }
            }
        }
        int h = 0;
        for(auto it = dist.begin(); it != dist.end(); it ++)
        {
            if(uf.Find(0) == uf.Find(m * n - 1))
                break;
            h = it->first;
            for(auto p: it->second)
                uf.Union(p.first, p.second);
        }
        return h;
    }
};