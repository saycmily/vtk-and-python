class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> ans;
        long cur = 1;
        for (int i = 0; i < rowIndex+1; ++i) {
            ans.emplace_back((int)cur);
            cur = cur * (rowIndex-i)/(i+1);
        }
        return ans;
    }
};