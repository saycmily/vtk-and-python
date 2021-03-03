class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        int n = nums.size();
        map<int, int> tongji;
        for (int i = 0; i < n; ++i) {
            if (tongji.find(nums[i]) == tongji.end())
                tongji[nums[i]] = 0;
            else 
                tongji[nums[i]] ++;
        }
        int cur = tongji[nums[0]];
        vector<int> m;
        for (auto it = tongji.begin(); it != tongji.end(); it ++) {
            int h = it->first;
            if (it->second > cur) {
                m.clear();
                m.emplace_back(h);
                cur = it->second;
            } else if (it->second == cur) {
                m.emplace_back(h);
            }
        }
        int l,r,ans=INT_MAX;
        for (int j = 0; j < m.size(); ++j) {
            l = find(nums.begin(), nums.end(), m[j]) - nums.begin();
            r = find(nums.rbegin(), nums.rend(), m[j]) - nums.rbegin();
            //cout << l << " " << r << " " << n-l-r << endl;
            ans = min(ans, n-l-r);
        }
        return ans;
    }
};