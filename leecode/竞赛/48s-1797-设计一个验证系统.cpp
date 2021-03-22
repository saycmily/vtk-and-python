class AuthenticationManager {
private:
    int timetolive;
    unordered_map<string, int> cun;
public:
    AuthenticationManager(int timeToLive) {
        timetolive = timeToLive;
    }
    
    void generate(string tokenId, int currentTime) {
        cun[tokenId] = currentTime;
    }
    
    void renew(string tokenId, int currentTime) {
        if (cun.count(tokenId) == 0)
            return;
        int oldtime = cun[tokenId];
        if (currentTime - oldtime >= timetolive)
            return;
        cun[tokenId] = currentTime;
    }
    
    int countUnexpiredTokens(int currentTime) {
        int ans = 0;
        for (auto it : cun) {
            if (it.second+timetolive > currentTime)
                ans ++;
        }
        return ans;
    }
};

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * AuthenticationManager* obj = new AuthenticationManager(timeToLive);
 * obj->generate(tokenId,currentTime);
 * obj->renew(tokenId,currentTime);
 * int param_3 = obj->countUnexpiredTokens(currentTime);
 */