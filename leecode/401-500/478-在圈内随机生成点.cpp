class Solution {
public:
    double r, x, y;
    Solution(double radius, double x_center, double y_center) {
        r = radius;
        x = x_center;
        y = y_center;
    }
    vector<double> randPoint() {
        double tx, ty;
        do {
            tx = 2 * (double)rand() / RAND_MAX - 1;
            ty = 2 * (double)rand() / RAND_MAX - 1;
        } while (tx * tx + ty * ty > 1);
        return {x + tx * r, y + ty * r};
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(radius, x_center, y_center);
 * vector<double> param_1 = obj->randPoint();
 */