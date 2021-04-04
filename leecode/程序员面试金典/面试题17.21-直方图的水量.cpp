class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int cur = 0, lsum = 0, rsum = 0, sum = 0;
        for (int i = 0; i < n; ++i) {
            if (height[i] > cur)
                cur = height[i];
            lsum += cur;
            sum += height[i];
        }
        cur = 0;
        for (int j = n-1; j >= 0; --j) {
            if (height[j] > cur)
                cur = height[j];
            rsum += cur;
        }
        return lsum + rsum - n * cur - sum;
    }
};