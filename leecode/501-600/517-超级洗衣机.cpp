class Solution {
public:
    int findMinMoves(vector<int>& machines) {
        int n  = machines.size();
        // 排除不能平均分的情况
        int sum = 0;
        for (int num : machines) sum += num;
        if (sum % n != 0) return -1;
        // 每个洗衣机的数量
        int jun = sum / n;
        vector<int> chayi;
        for (int num : machines)
            chayi.emplace_back(num - jun);
        int ans = INT_MIN;
        for (int i = 0; i < n-1; ++i) {
            ans = max(ans, abs(chayi[i]));
            ans = max(ans, chayi[i+1]);
            chayi[i+1] += chayi[i];
        }
        return max(ans, chayi[n-1]);

    }
};