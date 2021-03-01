class Solution {
public:
    vector<int> findNumOfValidWords(vector<string>& w, vector<string>& p) {
        unordered_map<int, int> hash;
        int n = w.size(), m = p.size();
        vector<int> ans(m);
        for(int i = 0; i < n; i++) {
            int t = 0;
            for(char c:w[i]) 
                t |= (1 << c - 'a');
            hash[t] ++;
        }

        for(int i = 0; i < m; i++) {
            int k = 0, t = p[i][0] - 'a';
            for(char c : p[i]) 
                k |= (1 << c - 'a');
            for(int j = k; j; j = (j-1) & k)
                if(j >> t & 1) 
                    ans[i] += hash[j];
        }

        return ans;
    }
};