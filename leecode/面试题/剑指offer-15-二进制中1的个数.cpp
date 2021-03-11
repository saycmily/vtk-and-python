class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ans = 0;
        while (n) {
            if (n % 2)
                ans ++;
            n /= 2;
        }
        return ans;
    }
};
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ans = 0;
        while (n) {
            if (n & 1)
                ans ++;
            n = n >> 1;
        }
        return ans;
    }
};