class Solution {
public:
    int findSubstringInWraproundString(string p) {
        if (p.size() < 2) 
            return p.size();
        vector<int> vecCount(26, 0);
        ++vecCount[p[0] - 'a'];

        for (int i = 0, j = 1; j < p.size(); ++j){
            if ((p[j] - p[j - 1] != 1) && (p[j - 1] - p[j] != 25)) 
                i = j;
            vecCount[p[j] - 'a'] = max(vecCount[p[j] - 'a'], j - i + 1);
        }
       return accumulate(vecCount.begin(), vecCount.end(), 0);
    }
};
