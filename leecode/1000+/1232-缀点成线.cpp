class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int n = coordinates.size();
        bool flag = false;
        double k;
        if (n < 3) return true;
        double a = coordinates[0][0];
        double b = coordinates[0][1];
        double c = coordinates[1][0];
        double d = coordinates[1][1];
        if (a == c) 
            flag = true;
        else
            k = (d - b) / (c - a);
        for (int i = 2; i < n; ++i) {
            double e = coordinates[i][0];
            double f = coordinates[i][1];
            if (flag) {
                if (a != e) return false; 
            } else {
                double k1 = (f - b) / (e - a);
                if (k1 != k) return false;
            }
        }
        return true;
    }
};