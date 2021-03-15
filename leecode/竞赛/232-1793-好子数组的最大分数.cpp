class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        int n = nums.size();
        int i = k, j = k, res = nums[k], t = nums[k];
        while (true) {
            while(i >= 0 && nums[i] >= t){
                i--;
            }
            while(j < n && nums[j] >= t){
                j++;
            }
            res = max(res, t * (j - i - 1));
            if(i == -1 && j == n) break;
            if(i >= 0 && j < n) 
                t = max(nums[i], nums[j]);
            else if (i >= 0)
                t = nums[i];
            else
                t = nums[j];
        }
        return res;
    }
};