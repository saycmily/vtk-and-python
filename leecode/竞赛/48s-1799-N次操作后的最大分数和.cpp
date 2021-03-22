class Solution {
public:
    int maxScore(vector<int>& nums) {
        int n = nums.size();
        vector<int> f(1 << n);

        for(int i = 1; i < 1 << n; i++) {
            int cnt = __builtin_popcount(i);
            // 数字个数为奇数跳过
            if(cnt & 1) continue;
            cnt /= 2;
            for(int j = 0; j < n; j++)
                //第j位和第k位必须为1，才能继续。
                if(i >> j & 1)
                    for(int k = j + 1; k < n; k++)
                        if(i >> k & 1)
                            // 记录一种状态，^ - 都可。
                            f[i] = max(f[i], f[i - (1 << j) - (1 << k)] + cnt * gcd(nums[j], nums[k]));
        }
        return f.back();
    }
};