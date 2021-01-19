struct unionfind {
    vector<int> f;
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
        f[p] = q;
        return p == q;
    }
};
struct edge {
    int a, b, c;
    edge(int x, int y, int z): a(x), b(y), c(z) {}
    bool operator < (const edge& other) {
        return c < other.c;
    }
};
class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        unionfind uf(n);
        vector<edge> costs;
        for (int i = 0; i < n-1; ++i) {
            for (int j = i+1; j < n; ++j) {
                int xi = points[i][0], yi = points[i][1];
                int xj = points[j][0], yj = points[j][1];
                int cost = abs(xi-xj) + abs(yi-yj);
                costs.emplace_back(edge(i, j, cost));
            }
        }
        int ans = 0, ant = 0;
        sort(costs.begin(), costs.end());
        for (auto& edge : costs) {
            if (uf.merge(edge.a, edge.b)) continue;
            ans += edge.c;
            ant += 1;
            if (ant == n-1) break;
        }
        return ans;
    }
};