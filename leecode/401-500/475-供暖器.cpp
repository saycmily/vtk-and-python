class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        sort(houses.begin(), houses.end());
        sort(heaters.begin(), heaters.end());
        int m = houses.size();
        int n = heaters.size();
        int res = 0;
        int cur_heater = 0;
        for (int& house : houses) {
            while (cur_heater < n && heaters[cur_heater] < house)
                cur_heater++;
            if (cur_heater == 0)
                res = max(res, heaters[cur_heater] - house);
            else if (cur_heater == n)
                return max(res, houses[m-1] - heaters[n-1]);
            else
                res = max(res, min(heaters[cur_heater]-house, house-heaters[cur_heater-1]));
        }
        return res;
    }
};