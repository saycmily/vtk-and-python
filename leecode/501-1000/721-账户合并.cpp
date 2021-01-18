struct unionfind {
    vector<int> f;
    unionfind(int size) {
        f.resize(size);
        for (int i = 0; i < size; ++i) {
            f[i] = i;
        }
    }
    int find(int x) {
        if (x == f[x]) return x;
        return f[x] = find(f[x]);
    }
    void merge(int a, int b) {
        int q = find(a), p = find(b);
        f[q] = p;
    }
};
class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        vector<vector<string> > res;
        // yi <邮箱，账户id>
        unordered_map<string, int> yi;
        int n = accounts.size();
        unionfind uf(n);
        for (int i = 0; i < n; ++i) {
            int m = accounts[i].size();
            for (int j = 1; j < m; ++j) {
                string s = accounts[i][j];
                if (yi.find(s) == yi.end()) 
                    yi[s] = i;
                else
                    uf.merge(i, yi[s]);
            }
        }
        // iy <账户id, <邮箱列表> >
        unordered_map<int, vector<string> > iy;
        for (auto& [k, v] : yi) 
            iy[uf.find(v)].emplace_back(k);

        for (auto& [k, v] : iy){
            sort(v.begin(), v.end());
            vector<string> tmp = {accounts[k][0]};
            tmp.insert(tmp.end(), v.begin(), v.end());
            res.emplace_back(tmp);
        } 
        return res;
    }
};