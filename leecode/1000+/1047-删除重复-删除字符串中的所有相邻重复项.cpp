class Solution {
public:
    string removeDuplicates(string S) {
        if (S.length() < 2) return S;
        int cur = 0;
        int l = S.length();
        while (cur < l) {
            if (S[cur] == S[cur+1]) {
                S.erase(cur, 2);
                l -= 2;
                if (cur != 0) cur --;
            } else {
                cur ++;
            }
        }
        return S;
    }
};