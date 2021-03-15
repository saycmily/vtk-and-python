class Node{
public:
    int cost; 
    int profit;
    Node(int c, int p) : cost(c), profit(p){}
};
// 优先队列的比较器 按照花费从小到大排序
struct minCompare{
    bool operator()(Node n1, Node n2){
        return n1.cost > n2.cost;
    }
};
// 优先队列的比较器 按照利润从大到小排序
struct maxCompare{
    bool operator()(Node n1, Node n2){
        return n1.profit < n2.profit;
    }
};
class Solution {
public:
    int findMaximizedCapital(int k, int W, vector<int>& Profits, vector<int>& Capital) {
        // 全部构造节点
        // 按照花费 从小到大的优先队列
        priority_queue<Node, vector<Node>, minCompare> minCost;
        // 按照利润 从大到小的优先队列
        priority_queue<Node, vector<Node>, maxCompare> maxPro;
        // 全部加入到小根堆中
        for(int i = 0; i < Profits.size(); i++)
            minCost.push(Node(Capital[i], Profits[i]));

        while (k--) {
            while(!minCost.empty() && minCost.top().cost <= W){
                maxPro.push(minCost.top());
                minCost.pop();
            }
            if(maxPro.empty()){
                return W;
            }
            // 求当前profit
            W += maxPro.top().profit;
            maxPro.pop();
        }
        return W;
    }
};