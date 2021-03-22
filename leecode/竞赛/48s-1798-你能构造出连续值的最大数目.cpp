class Solution {
public:
    int getMaximumConsecutive(vector<int>& coins) {
        sort(coins.begin(), coins.end());
        int cur = 0;
        for(int i = 0; i < coins.size(); i++){
            if(coins[i] > cur + 1)
                break;
            cur += coins[i];
        }
        return cur + 1;
    }
};