class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& A) {
        int cur = 0;
        vector<bool> ans;
        for (int i = 0; i < A.size(); ++i) {
            cur = cur << 1;
            cur += A[i];
            if (cur % 5 == 0) {
                ans.emplace_back(true);
            } else {
                ans.emplace_back(false);
            }
            cur = cur % 5;
        }
        return ans;
    }
};
