class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int n = nums.size();
        int cur = 0, ans = 0;
        for (int i = 0; i < n; ++i) {
            if (nums[i] == 1) {
                cur ++;
            } else {
                ans = max(ans, cur);
                cur = 0;
            }
        }
        if (nums[n-1] == 1) 
            ans = max(ans, cur);
        return ans;
    }
};