class Solution {
public:
    vector<int> constructRectangle(int area) {
        int a = pow(area, 1.0/2);
        int L, W;
        for (W = a; W > 1; W --) {
            if (area % W == 0) 
                return {area/W, W};
        }
        return {area, 1};
    }
};