class Solution {
public:
    int row, col, sum;
    unordered_map<int, int> m;
    Solution(int n_rows, int n_cols) {
        col = n_cols;  row = n_rows;
        sum = n_cols * n_rows;
    }
    vector<int> flip() {
        int index = rand() % sum;
        while (m.count(index))
            index = m[index];
        m[index] = --sum;
        return {index / col, index % col};
    }
    
    void reset() {
        sum = col * row;
        m.clear();
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(n_rows, n_cols);
 * vector<int> param_1 = obj->flip();
 * obj->reset();
 */