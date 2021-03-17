class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        if (k == 0) {
            int shu = 0;
            for (int num : nums)
                if (num == 0) {
                    shu ++;
                    if (shu > 1)
                        return true;
                } else {
                    shu = 0;
                }
            return false;
        } 
        int n = nums.size();
        for (int& num : nums)
            num = num % k;
        for (int i = 0; i < n-1; ++i) {
            int cur_sum = nums[i];
            for (int j = i+1; j < n; ++j) {
                cur_sum += nums[j];
                if (cur_sum % k == 0)
                    return true;
            }
        }
        return false;

    }
};