class Solution {
public:
    string convertToBase7(int num) {
        string res = "";
        bool flag = false;
        if (num == 0)
            return "0";
        if (num < 0)
            flag = true;
        num = abs(num);
        while (num != 0) {
            int a = num % 7;
            num /= 7;
            res += to_string(a);
        }
        reverse(res.begin(), res.end());
        if (flag)
            return "-" + res;
        return res;
    }
};