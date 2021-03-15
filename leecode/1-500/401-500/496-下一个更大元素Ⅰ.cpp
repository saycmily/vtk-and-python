class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size();
        int n2 = nums2.size();
        vector<int> ans;
        for (int i = 0; i < n1; ++i) {
            int cur = nums1[i];
            bool flag = false;
            vector<int>::iterator it;
            for (it = find(nums2.begin(), nums2.end(), cur); it != nums2.end(); it++) {
                if (*it > cur){
                    ans.emplace_back(*it);
                    flag = true;
                    break;
                }
            }
            if (!flag) ans.emplace_back(-1);
        }
        return ans;
    }
};