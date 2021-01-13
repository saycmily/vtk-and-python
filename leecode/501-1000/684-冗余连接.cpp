struct unionfind {
    vector<int> f;
    unionfind(int size) {
        f.resize(size+1);
        for (int i = 1; i <= size; ++i)
            f[i] = i;
    }
    int find(int x) {
        if (x == f[x]) return x;
        return f[x] = find(f[x]);
    }
    bool merge(int a, int b) {
        int p = find(a), q = find(b);
        if (p == q) return true;
        f[p] = q;
        return false;
    }
};
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        unionfind uf(n);
        //查询连接的两个节点是否在同一连通域内;
        for (auto& edge : edges) 
            if (uf.merge(edge[0], edge[1]))
                return edge;
        return vector<int> {};
    }
};