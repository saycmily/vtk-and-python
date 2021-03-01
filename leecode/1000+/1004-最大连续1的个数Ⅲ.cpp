class Solution {
public:
    int longestOnes(vector<int>& A, int K) {
        int n = A.size();
        int num = 0, cur = 0, ans = 0;
        queue<int> l;
        for (int i = 0; i < n; ++i) {
            if (A[i] == 0) {
                l.push(i);
                num ++;
                if (num == K+1) {
                    ans = max(ans, cur);
                    cur = i - l.front() - 1;
                    l.pop();
                    num --;
                }
            }
            cur ++;
        }
        return max(ans, cur);
    }
};