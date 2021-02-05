class Solution {
public:
    string licenseKeyFormatting(string S, int K) {
    	stack<char> tStack;
	    string ans = "";
	    int cnt = 0;
	    for (auto c : S)
		    if(c != '-') tStack.push(c);
	    while (!tStack.empty()) {
		    ans.push_back(toupper(tStack.top()));
            tStack.pop();
		    cnt ++;
		    if (cnt % K == 0 && tStack.size() != 0)
		    	ans.push_back('-');
    	}
	    reverse(ans.begin(), ans.end());
	    return ans;
    }
};