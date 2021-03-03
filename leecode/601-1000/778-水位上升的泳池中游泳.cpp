struct node{
    int x,y,h;
    node(int _x,int _y,int _h){
        x = _x, y = _y, h = _h;
    }
    bool operator<(const node& other) const{
        return h > other.h; // 高度小的优先
    }
};
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
    void merge(int i, int j) {
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
    int swimInWater(vector<vector<int>>& grid) {
        m = grid.size(); // n 行
        n = grid[0].size(); // m 列
        priority_queue<node> pq;
        for(int x = 0; x < n; x++) {
            for(int y = 0; y < m; y++) {
                if (x > 0) 
                    pq.emplace(node(GetIndex(x, y), GetIndex(x-1, y), max(grid[x][y], grid[x-1][y])));
                if (y > 0)
                    pq.emplace(node(GetIndex(x, y), GetIndex(x, y-1), max(grid[x][y], grid[x][y-1])));
            }
        }// for
        UnionFind uf(n * m);
        while(!pq.empty()) {
            node t = pq.top(); 
            pq.pop();
            uf.merge(t.x, t.y);
            if (uf.Find(0) == uf.Find(n * m - 1))
                return t.h;
        }
        return 0;
    }
};
