class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int n = nums.size();
        int res = 0;
    
        for (int i = 0; i < 31; ++i) {
            int onecount = 0, cur = 0;
            for (int& num : nums) {
                onecount += num & 1;
                num >>= 1;
                cur += (num == 0 ? 1 :0);
            }
            res += onecount * (n - onecount);
            if (cur == n) break;
        }
        return res;
    }
};
