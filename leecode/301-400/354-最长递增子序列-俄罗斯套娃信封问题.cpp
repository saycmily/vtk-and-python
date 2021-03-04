class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        sort(envelopes.begin(), envelopes.end(),
            [](const vector<int> &a, const vector<int> &b) -> bool {
                if (a[0] == b[0]) 
                    return a[1] > b[1];
                return a[0] < b[0];
            });
        // set有序，最长递增序列
        set<int> a;
        for (auto e : envelopes) {
            int v = e[1];
            auto it = lower_bound(a.begin(), a.end(), v);
            if (it != a.end())
                a.erase(it);
            a.insert(v);
        }
        return a.size();
    }
};