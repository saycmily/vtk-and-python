struct unionfind {
    vector<int> f;
    int count = 0;
    unionfind(int size) {
        f.resize(size);
        count = size;
        for (int i = 0; i < size; ++i)
            f[i] = i;
    }
    int find(int x) {
        if (x == f[x]) return x;
        return f[x] = find(f[x]);
    }
    void merge(int a, int b) {
        int p = find(a), q = find(b);
        if (p == q) return;
        count --;
        f[q] = p;
    }
    int get_count() {
        return count;
    }
};
class Solution {
public:
    int minSwapsCouples(vector<int>& row) {
        int n = row.size();
        unionfind uf(n);
        for (int i = 0; i < n; i += 2) {
            uf.merge(i, i+1);
            uf.merge(row[i], row[i+1]);
        }
        return n / 2 - uf.get_count();
    }
};