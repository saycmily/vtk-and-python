class Solution {
public:
    bool judgeSquareSum(int c) {
        for(int i = 0; i <= sqrt(c); i++) {
            double a = sqrt(c - i*i);
            if(int(a) == a)
                return true;
        }
        return false;
    }
};