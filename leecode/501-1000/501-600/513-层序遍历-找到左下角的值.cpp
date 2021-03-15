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
    vector<vector<int>> levels; 
    int findBottomLeftValue(TreeNode* root) {
        queue<TreeNode*> q;
        q.emplace(root);
        vector<int> ceng;
        while (!q.empty()) {
            ceng.clear();
            int s = q.size();
            while (s --) {
                TreeNode* node = q.front();
                q.pop();
                ceng.emplace_back(node -> val);
                if (node -> left)
                    q.emplace(node -> left);
                if (node -> right)
                    q.emplace(node -> right);
            }
            levels.emplace_back(ceng);
        } 
        int n = levels.size();
        return levels[n-1][0];
    } 
};