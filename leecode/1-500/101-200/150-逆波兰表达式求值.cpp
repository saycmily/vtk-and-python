class Solution {
public:
    bool AllisNum(string str) {
        int i = 0;
        if (str[0] == '-' && str.length() != 1)
            i = 1;
        for (i; i < str.length(); ++i) {
            char tmp = str[i];
            if ('0' <= tmp && tmp <= '9')
                continue;
            else
                return false;
        }
        return true;
    }  
    int evalRPN(vector<string>& tokens) {
        stack<int> numbers;
        for (string s : tokens) {
            if (AllisNum(s)) {
                int is = stoi(s);
                numbers.push(is);
                continue;
            }
            int a = numbers.top(); numbers.pop();
            int b = numbers.top(); numbers.pop();
            if (s == "+")
                numbers.push(a + b);
            else if (s == "-") 
                numbers.push(b - a);
            else if (s == "/")
                numbers.push(b / a);
            else
                numbers.push(a * b);
        }
        return numbers.top();
    }
};