class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        int n = edges.size() +  1;
        vector<int> rudu(n, 0);
        for (vector<int> pair : edges) {
            rudu[pair[0]-1] ++;
            rudu[pair[1]-1] ++;
        }
        for (int i = 0; i < n; ++i) {
            if (rudu[i] == n-1)
                return i+1;
        }
        return 0;
    }
};