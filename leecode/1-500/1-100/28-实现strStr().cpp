class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = haystack.length();
        if(needle.length() == 0) return 0;
        int l = 0;
        while(l < n){
            if(needle[0] != haystack[l]) {
                l++;
                continue;
            }
            int cur1 = 0, cur2 = l;
            while(cur2 < n && needle[cur1] == haystack[cur2]){
                cur1++;
                cur2++;
            }
            if(cur1 == needle.length())
                return l;
            l++;
        }
        return -1;
    }
};