/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        vector<vector<int>> ans;
        map<int, vector<int>> tmp;
        queue<pair<TreeNode*, int>> q;
        q.push(make_pair(root, 0));
        while(!q.empty()) {
            int s = q.size();
            map<int,vector<int>> mp;
            while (s --) {
                pair<TreeNode*, int> cur = q.front(); q.pop();
                int ind = cur.second;
                if (mp.count(ind) == 0)
                    mp[ind] = vector<int>();
                mp[ind].emplace_back(cur.first -> val);
                if (cur.first -> left) 
                    q.push(make_pair(cur.first->left, ind-1));
                if (cur.first -> right)
                    q.push(make_pair(cur.first->right, ind+1));
            }
            for (auto it : mp) {
                vector<int> cur = it.second;
                sort(cur.begin(), cur.end());
                tmp[it.first].insert(tmp[it.first].end(), cur.begin(), cur.end());
            }
        }
        for (auto it : tmp)
            ans.emplace_back(it.second);
        return ans;
    }
};