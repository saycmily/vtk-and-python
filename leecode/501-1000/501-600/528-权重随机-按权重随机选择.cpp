class Solution {
public:
    vector<int> presum;
    int sum = 0;
    Solution(vector<int>& w) {
        for(int cur : w) {
            sum += cur;
            presum.emplace_back(sum);
        }
    }
    
    int pickIndex() {
        int n = rand() % sum + 1;
        return lower_bound(presum.begin(), presum.end(), n) - presum.begin();
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */