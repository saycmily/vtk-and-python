class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int n = nums.size();
        int i = 0, cur = nums[0], ans = nums[0];
        while(i < n-1) {
            if (nums[i] < nums[i+1])
                cur += nums[i+1];
            else 
                cur = nums[i+1];
            ans = max(ans, cur);
            i ++;
        }
        return ans;
    }
};