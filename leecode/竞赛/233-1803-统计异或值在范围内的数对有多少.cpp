const int N = 1e5;
class Solution {
public:
    int son[N][2], cnt[N], idx=0;
    void insert(int x) {
        int p = 0;
        for(int i = 16; i >= 0; --i) {
            int u = x >> i & 1;
            if(!son[p][u]) son[p][u] = ++idx;
            p = son[p][u];
            cnt[p] ++;
        }
    }
    int query(int x, int high) {
        int res = 0, p = 0;
        for(int i = 16; i >= 0; --i) {
            int u = x >> i & 1, h = high >> i & 1;
            if (h == 1) {
                res += cnt[son[p][u]];
                p = son[p][1-u];
            } else
                p = son[p][u];
            if(!p) return res;
        }
        return res;
    }
    int countPairs(vector<int>& nums, int low, int high) {
        int res = 0;
        for(int i : nums) {
            res += query(i, high + 1) - query(i, low);
            insert(i);
        } 
        return res;
    }
};