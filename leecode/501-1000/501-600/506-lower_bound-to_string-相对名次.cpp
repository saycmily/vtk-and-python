class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        int n = score.size();
        vector<int> clone = score;
        sort(score.begin(), score.end());
        vector<string> ans;
        for (int i = 0; i < n; ++i) {
            int it = lower_bound(score.begin(), score.end(), clone[i]) - score.begin();
            if (it == n-1)
                ans.emplace_back("Gold Medal");
            else if (it == n-2)
                ans.emplace_back("Silver Medal");
            else if (it == n-3)
                ans.emplace_back("Bronze Medal");
            else{
                int a = n - it;
                ans.emplace_back(to_string(a));
            }
        }
        return ans;
    }
};