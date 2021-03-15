#include <iostream>
#include <string>
#include <regex>
using namespace std;

class Solution {
public:
    string validIPAddress(string IP) {
        if (IP.empty()) {
            return "Neither";
        }
        // 双引号前加R目前测试了不可行
        regex regexIPv4("(\\d|[1-9]\\d|1\\d\\d|2[0-4]\\d|25[0-5])(\\.(\\d|[1-9]\\d|1\\d\\d|2[0-4]\\d|25[0-5])){3}");
        regex regexIPv6("([0-9a-fA-F]{1,4}\\:){7}[0-9a-fA-F]{1,4}");
        string result = "Neither";
        cmatch m;
        bool flag = regex_search("cao172.16.254.1yong", m, regexIPv4);
        if (flag) {
            cout << m.size() << endl;
            cout << m.str(0) << endl;
            cout << m.str(1) << endl;
            cout << m.str(2) << endl;
            cout << m.str(3) << endl;
            cout << m.prefix().str() << endl;
            cout << m.suffix().str() << endl;
        }
        if (regex_match(IP, regexIPv4)) {
            result = "IPv4";
        } else if (regex_match(IP, regexIPv6)) {
            result = "IPv6";
        }
        return result;
    }
};

int main() {
    Solution a = Solution();
    string b = a.validIPAddress("172.16.254.1");
    cout << b << endl;
    system("pause");
    return 0;
}