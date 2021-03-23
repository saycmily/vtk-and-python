class Solution {
public:
    int getNumberOfBacklogOrders(vector<vector<int>>& orders) {
        auto cmpMin = [](pair<int,int> p1,pair<int,int> p2){
            return p1.first > p2.first;  
        };
        priority_queue<pair<int,int>> buyq;
        priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(cmpMin)> sellq(cmpMin);
        for(vector<int> ord : orders){
            int prc = ord[0];
            int amt = ord[1];
            if (ord[2] == 0) {    //buy
                while (amt && !sellq.empty()) {
                    pair<int, int> sellord = sellq.top();
                    if (prc >= sellord.first) {
                        sellq.pop();
                        if(sellord.second <= amt)
                            amt -= sellord.second;
                        else {
                            sellord.second -= amt;
                            sellq.emplace(sellord);
                            amt = 0;
                        }
                    }
                    else    
                        break;
                }
                if(amt)
                    buyq.emplace(prc,amt);
            } else {   //sell
                while(amt && !buyq.empty()){
                    pair<int, int> buyord = buyq.top();
                    if(prc <= buyord.first){
                        buyq.pop();
                        if(buyord.second <= amt)
                            amt -= buyord.second;
                        else {
                            buyord.second -= amt;
                            buyq.emplace(buyord);
                            amt = 0;
                        }
                    }
                    else    
                        break;
                }
                if(amt)     
                    sellq.emplace(prc,amt);
            }
        }
        int mod = 1e9+7;
        long ans = 0;
        while(!buyq.empty()){
            ans += buyq.top().second; 
            buyq.pop();
        }
        while(!sellq.empty()){
            ans += sellq.top().second; 
            sellq.pop();
        }
        return ans % mod;
    }
};