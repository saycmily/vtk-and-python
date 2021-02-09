class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        int n = arr.size();
        if (n == 1) return 1;
        if (n == 2) {
            if (arr[0] == arr[1]) return 1;
            return 2;
        }
        int cur = 0, ans = 0; 
        for (int i = 1; i < n-1; ++i) {
            if (arr[i-1] == arr[i]) {
                ans = max(ans, i - cur);
                cur = i;
                continue;
            }
            if (arr[i] == arr[i+1]) {
                ans = max(ans, i - cur + 1);
                cur = i;
                continue;
            }
            if ((arr[i-1] < arr[i]) ^ (arr[i] > arr[i+1])) {
                ans = max(ans, i - cur + 1);
                cur = i;
            }
        }
        if ((arr[n-3] < arr[n-2]) ^ (arr[n-2] < arr[n-1]))
            ans = max(ans, n - cur);
        return ans;
    }
};