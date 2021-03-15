class Solution {
public:
    int largestPalindrome(int n) {
        int up = pow(10, n) - 1;
        int down = pow(10, n - 1);
        for (int h = 0; h < 2; ++h) {
            for (int v = up; v >= down; --v) {
                string left = to_string(v);
                string right(left.rbegin() + h, left.rend());
                long p = stoll(left + right);
                for (long k = up; k * k >= p; --k)
                    if (p % k == 0) return p % 1337;
            }
        }
        return -1;
    }
};