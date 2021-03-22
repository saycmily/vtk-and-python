class Solution {
public:
    int secondHighest(string s) {
        set<int> stc;
        for (char c : s) {
            if ('0' <= c && c <= '9') 
                stc.insert(c - '0');
        }
        int n = stc.size();
        if (n <= 1)
            return -1;
        int x = 0;
        for (int i : stc) {
            if (x == n - 2)
                return i;
            x++;
        }
        return -1;
    }
};