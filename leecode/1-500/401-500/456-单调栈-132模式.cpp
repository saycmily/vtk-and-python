class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        stack<int> z;
        int mi = INT_MIN;
        for (int i = nums.size()-1; i >= 0; --i) {
            if (nums[i] < mi)
                return true;
            while(!z.empty() && nums[i] > z.top()) {
                mi = z.top();
                z.pop();
            } 
            z.push(nums[i]);
        }
        return false;
    }
};