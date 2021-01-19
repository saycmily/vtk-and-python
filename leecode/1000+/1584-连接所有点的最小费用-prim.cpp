class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size(), res = 0;
        int gra[1005][1005], dis[1005], flag[1005] = {0};
        memset(dis, 0x3f, sizeof dis);
        for(int i = 0; i < points.size(); i++) {
            for(int j = 0 ;j < points.size(); j++) {
                gra[i][j] = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1]);
            }
        }
        for(int i = 0; i < n; i++) {
            int t = -1;
            for(int j = 0; j < n; j++)
                if(!flag[j] && (t == -1 || dis[t] > dis[j])) 
                    t = j;
            if (i) res += dis[t];
            flag[t] = 1;
            for(int j = 0; j < n; j++) 
                if (!flag[j]) dis[j] = min(dis[j], gra[t][j]);
        }
        return res;
    }
};