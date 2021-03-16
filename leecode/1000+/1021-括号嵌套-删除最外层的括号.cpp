class Solution {
public:
    string removeOuterParentheses(string S) {
        string ans = "";
        int du = 0;
        string str = "";
        for(char c : S) {
            if (c == '(') {
                du -= 1;
                if (du < -1) {
                    str += "(";
                }
            } else {
                du += 1;
                if (du == 0) {
                    ans += str;
                    str = "";
                } else if (du < 0) {
                    str += ')';
                }
            }
        } 
        return ans;
    }
};