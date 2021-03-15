class Solution {
public:
    int calculate(string s) {
        stack<int> numbers;
        stack<char> operators;
        int n = s.length();
        int i = 0;
        while (i < n) {
            if (s[i] == ' ') {
                i ++;
                continue;
            }
                
            if (s[i] == '+' || s[i] == '-') 
                operators.push(s[i]);
            else if (s[i] == '*' || s[i] == '/') {
                operators.push(s[i]);
            } else {
                int cur = i;
                int num = 0;
                while (i < n && s[i] >= '0' && s[i] <= '9') {
                    num = num * 10 + (s[i] - '0');
                    i++;
                }
                if (!operators.empty()) {
                    int tmp = numbers.top();
                    if (operators.top() == '*') {
                        numbers.pop();
                        operators.pop();
                        numbers.push(tmp * num);
                    } else if (operators.top() == '/') {
                        numbers.pop();
                        operators.pop();
                        numbers.push(tmp / num);
                    } else {
                        numbers.push(num);
                    }
                } else {
                    numbers.push(num);
                }
                i --;
            }
            i++;
        }
        int ans = 0;
        while (!operators.empty()) {
            int a = numbers.top(); numbers.pop();
            if (operators.top() == '+')
                ans += a;
            else 
                ans -= a;
            operators.pop();
        }
        return ans + numbers.top();
    }
};