class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num == 1) return false;
        int a = pow(num, 1.0/2) + 1;
        int sum = 0;
        for (int i = 2; i < a; ++i) {
            if (num % i == 0)
                sum += i + num/i;
        }
        return sum + 1 == num;
    }
};