class Solution {
public:
    bool zichuan(string a, string b) {
        int lena = a.length();
        int lenb = b.length();
        int pa = 0, pb = 0;
        while (pa < lena) {
            if (pb < lenb && a[pa] == b[pb])
                pb ++;
            pa ++;
        }
        return pb == lenb;
    }
    string findLongestWord(string s, vector<string>& dictionary) {
        vector<string> ans;
        for (string cur : dictionary)
            if(zichuan(s, cur))
                ans.emplace_back(cur);
        if (ans.empty())
            return "";
        sort(ans.begin(), ans.end(), [](string a, string b) {
            if (a.length() == b.length())
                return a < b;
            return a.length() > b.length();
        });
        return ans[0];
    }
};