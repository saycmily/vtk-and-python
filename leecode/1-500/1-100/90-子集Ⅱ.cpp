class Solution {
public:
    void backtrack(vector<vector<int>>& ans, vector<int> nums, vector<int>& tmp, int first) {
        ans.emplace_back(tmp);
        for(int i = first; i < nums.size(); ++i) {
            if (i != first && nums[i] == nums[i-1])
                continue;
            tmp.emplace_back(nums[i]);
            backtrack(ans, nums, tmp, i+1);
            tmp.pop_back();
        }
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        vector<int> tmp;
        backtrack(ans, nums, tmp, 0);
        return ans;
    }
};