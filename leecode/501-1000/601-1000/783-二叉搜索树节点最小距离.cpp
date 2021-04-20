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
    int minDiffInBST(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        vector<int> level;
        while(!q.empty()){
            int size = q.size();
            while(size--){
                TreeNode* p = q.front();
                q.pop();
                level.emplace_back(p->val);
                if(p -> left)
                    q.push(p->left);
                if(p -> right)
                    q.push(p->right);
            }
        }
        sort(level.begin(), level.end());
        int ans = INT_MAX;
        for(int i = 1; i < level.size(); ++i)
            ans = min(ans, level[i]-level[i-1]);
        return ans;
    }
};