class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int X) {
        int n = customers.size();
        int sum = 0;
        for (int i = 0; i < n; ++i) {
            if (grumpy[i] == 0)
                sum += customers[i];
        }
        for (int i = 0; i < X; ++i)
            if (grumpy[i] == 1)
                sum += customers[i];
        int ans = sum;
        int l = 0, r = X - 1;
        while(r+1 < n) {
            if (grumpy[l] == 1)
                sum -= customers[l];
            l ++;
            r ++;
            if (grumpy[r] == 1) 
                sum += customers[r];
            ans = max(ans, sum);
        }
        return ans;
    }
};