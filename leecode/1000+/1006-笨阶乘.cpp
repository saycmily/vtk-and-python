class Solution {
public:
    int clumsy(int N) {
        if (N == 1) return 1;
        else if (N == 2) return 2;
        else if (N == 3) return 6;
        int rest = N % 4;
        int ans = 0;
        for (int i = N; i >= 4; i-=4) {
            if (i == N)
                ans += i * (i-1) / (i-2) + i - 3;
            else 
                ans -= i * (i-1) / (i-2) - (i-3);
        }
        if (rest == 1)
            return ans - 1;
        else if (rest == 2)
            return ans - 2;
        else if (rest == 3)
            return ans - 6;
        return ans;
    }
};