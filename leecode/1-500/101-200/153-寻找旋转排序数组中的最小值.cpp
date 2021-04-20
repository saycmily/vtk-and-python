class Solution {
public:
    int findMin(vector<int>& nums) {
        int ex = nums[0];
        for(int i = 1; i < nums.size(); ++i)
            if (nums[i] < ex)
                return nums[i];
        return ex;
    }
};