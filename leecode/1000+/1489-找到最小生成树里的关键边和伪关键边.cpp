// 定义边结构体
struct edge{
    int i, s, e, w;
    edge(int a, int b, int c, int d):i(a), s(b), e(c), w(d){}
    bool operator < (const edge &g){ return w < g.w; }
};
class Solution {
private:
    // 并查集基本操作
    vector<int> parent;
    void init(int n){
        parent.clear();
        for (int i = 0; i < n; i++) {
            parent.push_back(i);
        }
    }
    int findParent(int num){
        int n = num;
        while (n != parent[n]) {
            n = parent[n];
        }
        return n;
    }
    bool unit(int s, int e) {
        int ns = findParent(s);
        int ne = findParent(e);
        if (ns != ne) {
            parent[ns] = ne;
            return true;
        }
        return false;
    }
public:
    int minMstV = 0;
    vector<edge> nums;
    vector<int> keyEdges, fakeEdges;

    // 主处理函数
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) {
        for (int i = 0; i < edges.size(); i++) {
            nums.push_back({i, edges[i][0], edges[i][1], edges[i][2]});
        }
        sort(nums.begin(), nums.end());
        // 求最小mst树的权值
        minMstV = deleteOneEdgeMst(n, {-1,-1,-1,-1});
        for (auto num:nums) 
            if (minMstV != deleteOneEdgeMst(n, num)) 
                keyEdges.push_back(num.i);
        
        unordered_set<int> setKeyEdges(keyEdges.begin(), keyEdges.end());
        for (auto num:nums) {
            // 需排除关键边
            if (setKeyEdges.find(num.i) != setKeyEdges.end())
                continue;
            if (addOneEdgeFirstMst(n, num) == minMstV)
                fakeEdges.push_back(num.i);
        }
        return {keyEdges, fakeEdges};
    }

    // 删除一条边求最小mst权值
    int deleteOneEdgeMst(int n, edge del) {
        init(n);
        int mstV = 0;
        int cnt = 0;
        for (auto num:nums) {
            if (num.i == del.i) {
                continue;
            }
            if (unit(num.s, num.e)) {
                cnt++;
                mstV += num.w;
            }
            if (cnt == n-1) break;
        }
        return mstV;
    }

    // 优先添加一条边后求最小mst权值
    int addOneEdgeFirstMst(int n, edge addEdge) {
        init(n);
        unit(addEdge.s, addEdge.e);
        int mstV = addEdge.w;
        int cnt = 1;
        for (auto num:nums) {
            if (num.i == addEdge.i) {
                continue;
            }
            if (unit(num.s, num.e)) {
                cnt++;
                mstV += num.w;
            }
            if (cnt == n-1) break;
        }
        return mstV;
    }
};