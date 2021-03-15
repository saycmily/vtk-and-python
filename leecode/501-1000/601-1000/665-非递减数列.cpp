class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        for (int i = 1; i < n-1; ++i) {
            if (nums[i-1] <= nums[i] && nums[i] <= nums[i+1])
                continue;
            if (nums[i-1] > nums[i] && nums[i] > nums[i+1])
                return false;
            if (nums[i-1] >= nums[i] && nums[i] <= nums[i+1]) {
                if (nums[i+1] >= nums[i-1])
                    nums[i] = nums[i-1];
                else 
                    nums[i-1] = nums[i];
            } else if (nums[i-1] <= nums[i] && nums[i] >= nums[i+1]) {
                if (nums[i+1] >= nums[i-1])
                    nums[i] = nums[i-1];
                else 
                    nums[i+1] = nums[i];
            }
            ans ++;
            if (ans > 1) return false;
        }
        return true;   
    }
};