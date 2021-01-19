class Solution {
public:
    bool backtrack(int i, vector<int>& sums, vector<int>& nums, int a) {
        if (i == nums.size()) return true;
        for (int j = 0; j < 4; ++j) {
            if (sums[j] + nums[i] > a) continue;
            if (j == 0 || sums[j] != sums[j-1]) {
                sums[j] += nums[i];
                if (backtrack(i+1, sums, nums, a))
                    return true;
                sums[j] -= nums[i];
            }
        }
        return false;
    }
    bool makesquare(vector<int>& nums) {
        int n = nums.size();
        int sum = 0;
        for (int i = 0; i < n; ++i)
            sum += nums[i];
        if (sum % 4 || n < 4) return false;
        sum = sum / 4;
        sort(nums.begin(), nums.end(), greater<int>());
        vector<int> sums = {0,0,0,0};
        if (sum < nums[0]) return false;
        return backtrack(0, sums, nums, sum);
    }
};