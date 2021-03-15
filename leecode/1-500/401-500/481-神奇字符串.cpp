class Solution {
public:
    int magicalString(int n) {
        if (n == 0) return 0;
        vector<int> nums(n+1);
        nums[0] = 1;
        int shuliang_index = 1;
        for (int i = 1; i < n; ++i) {
            if (nums[shuliang_index] == 1) {
                nums[i] = 3 - nums[i-1];
                shuliang_index ++;
                continue;
            }
            nums[i] = 3 - nums[i-1];
            i ++;
            nums[i] = nums[i-1];
            shuliang_index ++;
        }
        return count(nums.begin(), nums.end()-1, 1);
    }
};