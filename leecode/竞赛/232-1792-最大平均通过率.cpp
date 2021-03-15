class Solution {
public:
    // 自定义比较结构体
    struct mycmp {
        bool operator() (pair<int, int> a, pair<int, int> b){
            int x1 = a.first, y1 = a.second;
            int x2 = b.first, y2 = b.second;
            double cha1 = (x1 + 1) * 1.0 / (y1 + 1) - x1 * 1.0 / y1;
            double cha2 = (x2 + 1) * 1.0 / (y2 + 1) - x2 * 1.0 / y2;
            return cha1 < cha2;
	    }
    };
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        /* 自定义比较函数，优先队列声明较繁琐
        auto cmp = [](pair<int, int> a, pair<int, int> b) {
            int x1 = a.first, y1 = a.second;
            int x2 = b.first, y2 = b.second;
            double cha1 = (x1 + 1) * 1.0 / (y1 + 1) - x1 * 1.0 / y1;  
            double cha2 = (x2 + 1) * 1.0 / (y2 + 1) - x2 * 1.0 / y2;
            return cha1 < cha2;
        };
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> pq(cmp);
        */
        priority_queue<pair<int, int>, vector<pair<int, int>>, mycmp> pq;
        for (vector<int> x : classes) 
            pq.push(make_pair(x[0], x[1]));
        while(extraStudents --) {
            pair<int, int> tmp = pq.top();
            pq.pop();
            pq.push(make_pair(tmp.first+1, tmp.second+1));
        }
        double ans = 0.0;
        while(!pq.empty()) {
            pair<int, int> cur = pq.top();
            pq.pop();
            ans += cur.first * 1.0 / cur.second;
        }
        return ans / classes.size();
       
    }
};