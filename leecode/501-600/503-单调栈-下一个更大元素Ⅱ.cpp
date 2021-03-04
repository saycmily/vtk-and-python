class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n, -1);
        stack<int> sta;
        for(int i = 0; i<n; i++)
            nums.push_back(nums[i]);

        for(int i = 0; i<nums.size(); i++){
            while(!sta.empty() && nums[sta.top()] < nums[i]){
                if (sta.top() < n)
                    ans[sta.top()] = nums[i];
                sta.pop();
            }
            sta.push(i);
        }
        return ans;
    }
};