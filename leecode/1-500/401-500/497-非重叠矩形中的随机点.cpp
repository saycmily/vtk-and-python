class Solution {
public:
    vector<vector<int>> newrects;
    vector<int> presum;
    int sum = 0;
    Solution(vector<vector<int>> &rects) {
        newrects = rects;
        for (auto &rect : rects) {
            sum += (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1);
            presum.push_back(sum);
        }
    }
    vector<int> pick() {
        int n = rand() % sum + 1;
        int index = lower_bound(presum.begin(), presum.end(), n) - presum.begin();
        vector<int>& tmprect = newrects[index];
        int i = rand() % (tmprect[2] - tmprect[0] + 1) + tmprect[0];
        int j = rand() % (tmprect[3] - tmprect[1] + 1) + tmprect[1];
        return vector<int> {i, j};
    }
};