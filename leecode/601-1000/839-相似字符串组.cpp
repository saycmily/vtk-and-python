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
        if (p != q) {
            count --;
            f[p] = q;
        }
    }
    int get_count() {
        return count;
    }
};
class Solution {
public:
    int numSimilarGroups(vector<string>& strs) {
        int n = strs.size();
        unionfind uf(n);
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                if (isSimilar(strs[i], strs[j]))
                    uf.merge(i,j);
        return uf.get_count();
    }
private:
    bool isSimilar(string A, string B) {
        int cnt = 0;
        for(int i = 0; i < A.size(); i++)
            cnt += (A[i] != B[i]);
        return cnt <= 2;
    }
};