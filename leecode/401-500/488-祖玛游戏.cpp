class Solution {
private:
    int ans = INT_MAX;
    int cnt = 0;
    vector<int> h = vector<int>(26, 0);
public:
    int findMinStep(string board, string hand) {
        cnt = hand.size();
        for (auto c : hand) h[c - 'A']++;
        dfs(board, 0);
        return ans == INT_MAX ? -1 : ans;
    }
    void dfs(string board, int step) {
        shoot(board);
        if (board.empty()) {
            ans = min(ans, step);
            return;
        }
        if (step == cnt) return;
        if (step >= ans) return;

        set<pair<int, char>> ins;
        for (int i = 0; i < board.size(); i++) {
            int t = board[i] - 'A';
            // 如果后面的球和前面的球颜色不一样，插入后面的球
            if (i == 0 || board[i] != board[i - 1]) {
                if (h[t] != 0) 
                    ins.insert({ i, 'A' + t });
            }
            // 如果一样，在其中插入不同颜色
            if (i != 0 && board[i] == board[i - 1]) {
                for (int j = 0; j < h.size(); j++) {
                    if (j == t || h[j] == 0) continue;
                    ins.insert({ i, 'A' + j });
                }
            }
        }
        //回溯
        for (auto[i, c] : ins) {
            h[c - 'A']--;
            board.insert(i, 1, c);
            dfs(board, step + 1);
            board.erase(i, 1);
            h[c - 'A']++;
        }
    }
    //把爆炸的都去了
    void shoot(string& board) {
        for (int i = 0; i < (int)board.size() - 2; i++) {
            int j = i + 1;
            while (j < board.size() && board[i] == board[j]) j++;
            if (j - i < 3) {
                i = j - 1;
                continue;
            }
            board.erase(i, j - i);
            shoot(board);
            break;
        }
    }
};
