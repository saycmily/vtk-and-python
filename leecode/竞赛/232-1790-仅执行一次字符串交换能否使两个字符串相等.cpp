class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        if (s1 == s2) return true;
        int n1 = s1.length();
        int n2 = s2.length();
        if (n1 != n2) return false;
        int cur = 0;
        vector<char> num;
        for (int i = 0; i < n1; ++i) {
            if (s1[i] != s2[i]) {
                num.emplace_back(s1[i]);
                num.emplace_back(s2[i]);
                cur ++;
            } 
        }
        if (cur != 2) return false;
        if (num[0] == num[3] && num[1] == num[2]) return true;
        return false;
    }
};