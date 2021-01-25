class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int n = timeSeries.size();
        if (n == 0)
            return 0;
        int res = 0;
        for (int i = 1; i < n; ++i) {
            res += min(timeSeries[i] - timeSeries[i-1], duration);
        }
        return res + duration;
    }
};