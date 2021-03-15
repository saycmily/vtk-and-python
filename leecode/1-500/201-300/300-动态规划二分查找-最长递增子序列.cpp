class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n,1);
        int max = 0;
        for (int n : nums) {
            int left = 0, right = max;
            while (left < right) {
                int mid = (left + right) >> 1;
                if (dp[mid] < n) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            dp[left] = n;
            if (left == max)
                max ++;
        }
        return max;
    }
};