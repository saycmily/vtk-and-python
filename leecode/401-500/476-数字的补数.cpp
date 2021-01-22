class Solution {
public:
    int findComplement(int num) {
        vector<int> nums;
        while (num > 0) {
            int cur = 1 - num % 2;
            num = num / 2;
            nums.emplace_back(cur); 
        }
        int ans = 0;
        unsigned int cur = 1;
        for (int& i : nums) {
            ans += i*cur;
            cur = cur * 2;
        }
        return ans;
    }
};