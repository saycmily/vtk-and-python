class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        // int n = dominoes.size();
        // set<int> already;
        // int ans = 0;
        // for (int i = 0; i < n; ++i) {
        //     int cur = 1;
        //     if (already.count(i)) continue;
        //     already.insert(i);
        //     int a = dominoes[i][0], b = dominoes[i][1];
        //     vector<int> cha {b, a};
        //     for (int j = i+1; j < n; ++j) {
        //         if (dominoes[j] == cha || dominoes[j] == dominoes[i]) {
        //             cur ++;
        //             already.insert(j);
        //         }
        //     }
        //     ans += cur*(cur-1)/2;
        // }
        // return ans;
        // 计数排序
        int ans = 0;
        vector<int> cp(100, 0);
        for (auto& arr : dominoes) {
            int x = 0;
            if (arr[0] < arr[1])
                x = arr[0] * 10 + arr[1];
            else
                x = arr[1] * 10 + arr[0];
            ans += cp[x];
            cp[x] ++;
        }
        return ans;
    }
};