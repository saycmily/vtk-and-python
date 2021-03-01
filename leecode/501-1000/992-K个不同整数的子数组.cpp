class Solution {
public:
    int subarraysWithKDistinct(vector<int>& A, int K) {
        int ans = 0, size = A.size(), begin = 0, numCount = 0, end = begin, tmpEnd;
        vector<int> map(size + 1, 0);
        while(begin < size - K + 1) {
            // 先确定最小数组
            while(numCount < K && end < size){
                if(!map[A[end]]) ++numCount;
                ++map[A[end]];
                ++end;
            }
            if(numCount < K) 
                return ans;
            ++ans;
            tmpEnd = end;
            // 扩大最小数组至最大
            while(end < size && map[A[end]]) { 
                ++end; 
                ++ans; 
            }
            // 移动左边界
            if(--map[A[begin]] == 0) 
                --numCount;
            // tmpend意义：左边界不唯一，重计一边个数
            end = tmpEnd;
            ++begin;
        }
        return ans;
    }
};