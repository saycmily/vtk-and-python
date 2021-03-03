class Solution {
public:
    vector<int> addToArrayForm(vector<int>& A, int K) {
        int n = A.size();
        bool flag = false;
        for (int i = n-1; i >= 0; --i) {
            int cur = K % 10;
            K = K / 10;
            A[i] += cur;
            if (A[i] >= 10) {
                int x = A[i] / 10;
                A[i] = A[i] % 10;
                if (i == 0){
                    A.insert(A.begin(), x);
                    flag = true;
                } else {
                    A[i-1] += x;
                }
            }
        }
        if (flag){
            K += A[0];
            A.erase(A.begin());
        }
        while (K != 0) {
            int cur = K % 10;
            K = K / 10;
            A.insert(A.begin(), cur);
        }
        return A;
    }
};
