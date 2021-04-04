class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int m1 = 0, n1 = 0;
        vector<int> ans;
        while(m1 < m || n1 < n) {
            if (m1 == m) {
                ans.emplace_back(nums2[n1]);
                n1 ++;
                continue;
            } else if (n1 == n) {
                ans.emplace_back(nums1[m1]);
                m1 ++;
                continue;
            }
            if (nums1[m1] < nums2[n1]) {
                ans.emplace_back(nums1[m1]);
                m1 ++;
            }else{
                ans.emplace_back(nums2[n1]);
                n1 ++;
            }
        }
        nums1 = ans;
    }
};