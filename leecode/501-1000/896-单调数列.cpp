class Solution {
public:
    bool isMonotonic(vector<int>& A) {
        int n = A.size();
        int f = 0;
        bool flag;
        for (int i = 1; i < n; ++i) {
            if (A[i-1] == A[i]) continue;
            if (f == 0) {
                if (A[i-1] < A[i])
                    flag = true;
                else
                    flag = false;
                f = 1;
                continue;
            }
            if ((A[i-1] < A[i]) ^ flag)
                return false;
        }
        return true;
    }
};