class Solution {
public:
    int calculate(string s) {
        stack<int> numbers;
        stack<char> operators;
        int i = 0;
        if(!s.empty())
            while((i = s.find(' ',i)) != string::npos)
                s.erase(i, 1);
        s = '(' + s + ')';
        int n = s.length();
        i = 0;
        while (i < n) {
            //cout << i << endl;
            if (s[i] == '(' || s[i] == '+' || s[i] == '-') 
                operators.push(s[i]);
            else if (s[i] == ')') {
                int he = 0;
                while (operators.top() != '(') {
                    char op = operators.top(); operators.pop();
                    int number = numbers.top(); numbers.pop();
                    if (op == '-')
                        he -= number;
                    else
                        he += number;
                }
                operators.pop();
                if (!numbers.empty()) {
                    he += numbers.top(); 
                    numbers.pop();
                }
                numbers.push(he);
            } else {
                int cur = i;
                int num = 0;
                while (i < n && s[i] >= '0' && s[i] <= '9') {
                    num = num * 10 + (s[i] - '0');
                    i++;
                }
                if (cur > 1 && s[cur-1] == '-' && s[cur-2] == '(') {
                    operators.pop();
                    numbers.push(-num);
                } else
                    numbers.push(num);
                i --;
            }
            i++;
        }
        return numbers.top();
    }
};