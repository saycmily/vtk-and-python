class Solution {
public:
    int hammingDistance(int x, int y) {
        int z = x ^ y;
        int ans = 0;
        while (z) {
            // ans += z & 1;
            // z = z>>1;
            ans += 1;
            z = z & (z - 1);
        }
        return ans;
    }
};