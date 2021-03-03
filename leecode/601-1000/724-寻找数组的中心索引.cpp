class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size(), sum = 0;
        for (int i = 0; i < n; ++i)
            sum += nums[i];
        int cur_sum = 0;
        for (int i = 0; i < n; ++i)
            if (2 * cur_sum + nums[i] == sum)
                return i;
            else
                cur_sum += nums[i];
        return -1;
    }
};