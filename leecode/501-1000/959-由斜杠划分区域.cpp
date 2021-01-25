struct unionfind {
    vector<int> f;
    int count = 1;
    unionfind(int size) {
        f.resize(size);
        for (int i = 0; i < size; ++i)
            f[i] = i;
    }
    int find(int x) {
        if (x == f[x]) return x;
        return f[x] = find(f[x]);
    }
    void merge(int a, int b) {
        int p = find(a), q = find(b);
        if (p == q)
            count ++;
        else
            f[q] = p;
    }
    void define(int x) {
        f[x] = 0;
    }
    int get_count() {
        return count;
    }
};
class Solution {
public:
    int regionsBySlashes(vector<string>& grid) {
        int n = grid.size() + 1;
        int s = n * n;
        unionfind uf(s);
        for (int i = 0; i < n; ++i) {
            uf.define(i);
            uf.define(i * n);
            uf.define(i * n + n - 1);
            uf.define(n * (n - 1) + i);
        }
        for (int i = 0; i < n-1; ++i) {
            for (int j = 0; j < n-1; ++j) {
                if (grid[i][j] == '/') {
                    int fir = n * i + j + 1;
                    int sec = n * (i + 1) + j;
                    uf.merge(fir, sec);
                } else if (grid[i][j] == '\\') {
                    int fir = n * i + j;
                    int sec = n * (i + 1) + j + 1;
                    uf.merge(fir, sec);  
                }
            }
        }
        return uf.get_count();
    }
};