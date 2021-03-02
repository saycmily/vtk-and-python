class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        // 保存最小值队列和最大值队列
        deque<int> asc, desc;

        int left = 0, right = 0, res = 0;

        while (right < nums.size()) {
           //加入新元素，维护一下单调性
            while (!asc.empty() && nums[asc.back()] >= nums[right])
                asc.pop_back();
            while (!desc.empty() && nums[desc.back()] <= nums[right])
                desc.pop_back();

            asc.push_back(right);
            desc.push_back(right);
           //超过阈值了，缩窗口，维护最值
            while (abs(nums[desc.front()] - nums[asc.front()]) > limit) {
                left++;
                if (!asc.empty() && asc.front() < left)
                    asc.pop_front();
                if (!desc.empty() && desc.front() < left)
                    desc.pop_front(); 
            }
            res = max(res, right-left+1);
            right++;
        }
        return res;
    }
};