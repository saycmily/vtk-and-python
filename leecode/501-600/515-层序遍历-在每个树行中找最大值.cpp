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
    vector<int> largestValues(TreeNode* root) {
        if (root == nullptr)
            return {};
        queue<TreeNode*> q;
        q.emplace(root);
        vector<int> ceng;
        vector<int> ans;
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
            vector<int>::iterator it = max_element(ceng.begin(), ceng.end());
            ans.emplace_back(*it);
        }
        return ans;        
    }
};