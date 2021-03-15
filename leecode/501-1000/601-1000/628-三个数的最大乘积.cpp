class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        int n = nums.size();
        vector<int> fu;
        for (int i = 0; i < n; ++i) {
            if (nums[i] < 0)
                fu.emplace_back(nums[i]);
        }
        sort(fu.begin(), fu.end());
        sort(nums.begin(), nums.end(), greater<int>());
        int m = fu.size();
        if (m <= 1 || nums[0] < 0) return nums[0] * nums[1] * nums[2];
        return nums[0] * max(nums[1]*nums[2], fu[0]*fu[1]);
    }
};