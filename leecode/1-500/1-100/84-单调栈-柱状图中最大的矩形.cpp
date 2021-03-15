class Solution {
public:
    // 单调栈
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        stack<int> indexs;
        indexs.push(-1);
        int ans = 0;
        for(int i = 0; i < n; ++i) {
            while (indexs.size() > 1 && heights[i] <= heights[indexs.top()]) {
                int x = indexs.top(); indexs.pop();
                ans = max(ans, heights[x] * (i-indexs.top()-1));
                cout << ans << endl;
            }
            indexs.push(i);
        }
        int l = indexs.size();
        for(int i = 1; i < l; ++i) {
            int x = indexs.top(); indexs.pop();
            ans = max(ans, heights[x] * (n-indexs.top()-1));
            cout << heights[x] << " " << n-indexs.top()-1 << endl;
        }
        return ans;
    }
};