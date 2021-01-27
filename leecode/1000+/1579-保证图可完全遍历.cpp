struct unionfind {
    vector<int> f;
    int count = 0;
    unionfind(int size) {
        f.resize(size);
        for (int i = 0; i < size; ++i)
            f[i] = i;
    }
    int find(int x) {
        if (x == f[x]) return x;
        return f[x] = find(f[x]);
    }
    bool merge(int a, int b) {
        int p = find(a), q = find(b);
        if (p == q) return true;
        f[q] = p;
        count ++;
        return false;
    }
    bool bianli(int size) {
        if (count == size - 1)
            return false;
        return true;
    }
};
class Solution {
public:
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        unionfind both(n+1);
        int ans = 0;
        for (auto& edge : edges)
            if (edge[0] == 3 && both.merge(edge[1], edge[2]))
                ans ++;
        unionfind Alice = both, Bob = both;
        for (auto& edge : edges) {
            if (edge[0] == 1 && Alice.merge(edge[1], edge[2]))
                ans ++;
            if (edge[0] == 2 && Bob.merge(edge[1], edge[2]))
                ans ++;
        }
        if (Alice.bianli(n) || Bob.bianli(n))
            return -1;
        return ans;
    }
};