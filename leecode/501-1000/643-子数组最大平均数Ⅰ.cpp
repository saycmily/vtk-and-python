class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int n = nums.size();
        double cur = 0;
        for (int i = 0; i < k; ++i) 
            cur += nums[i];
        double ans = cur;
        for (int i = k; i < n; ++i) {
            cur += nums[i] - nums[i-k];
            ans = max(ans, cur);
        }
        return ans / k;
    }
};