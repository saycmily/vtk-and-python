class Solution {
public:
    int count = 0;
    int countArrangement(int n) {
        vector<bool> visited(n+1, false);
        backtrack(n, 1, visited);
        return count;
    }
    void backtrack(int n, int pos, vector<bool>& visited) {
        if (pos > n) count ++;
        for (int i = 1; i <= n; ++i)
            if (!visited[i] && (pos % i == 0 || i % pos == 0)) {
                visited[i] = true;
                backtrack(n, pos + 1, visited);
                visited[i] = false;
            }
    }
};
