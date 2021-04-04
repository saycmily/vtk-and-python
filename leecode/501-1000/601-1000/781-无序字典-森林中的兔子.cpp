class Solution {
public:
    int numRabbits(vector<int>& answers) {
        if (answers.size() == 0) return 0;
        unordered_map<int, int> mp;
        int ans = 0;
        for (int num : answers) {
            if (num == 0) {
                ans ++;
                continue;
            }
            if (mp.count(num) == 0)
                mp[num] = 1;
            else
                mp[num] ++;
        }
        for(auto it : mp) {
            if(it.first+1 >= it.second)
                ans += it.first + 1;
            else {
                int cur = it.first + 1;
                if (it.second % cur == 0)
                    ans += cur * (it.second / cur);
                else
                    ans += cur * (it.second / cur + 1);
            }
        }
        return ans;
    }
};