class Solution {
public:
    vector<double> medianSlidingWindow(vector<int> &nums, int k){
        vector<double> result;
        vector<int> newnums;
        int left = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (i < k - 1) {
                newnums.insert(upper_bound(newnums.begin(), newnums.end(), nums[i]), nums[i]);
                continue;
            }
            newnums.insert(upper_bound(newnums.begin(), newnums.end(), nums[i]), nums[i]);
            result.push_back(((double)newnums[(k - 1) / 2] + (double)newnums[k / 2]) / 2);
            newnums.erase(lower_bound(newnums.begin(), newnums.end(), nums[left]));
            left++;
        }
        return result;
    }
};