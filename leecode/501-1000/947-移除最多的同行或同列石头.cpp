struct unionfind {
    vector<int> f;
    vector<int> rank;
    int count = 0;
    unionfind(int size) {
        f.resize(size);
        rank.resize(size);
        for (int i = 0; i < size; ++i) {
            f[i] = i;
        }
    }
    int find(int x) {
        if (x == f[x]) return x;
        return f[x] = find(f[x]);
    }

    void merge(int a, int b) {
        int p = find(a), q = find(b);
        if (p != q) {
            if (rank[p] <= rank[q])
                f[p] = q;
            else
                f[q] = p;
            if (rank[p] == rank[q])
                rank[q] += 1;
            count += 1;
        }
    }
    int get_count() {
        return count;
    }
};
class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
        int n = stones.size();
        unionfind uf(n);
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1]) {
                    uf.merge(i, j);
                }
            }
        }
        return uf.get_count();
    }
};