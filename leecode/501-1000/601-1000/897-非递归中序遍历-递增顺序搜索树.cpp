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
    TreeNode* increasingBST(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> st;
        TreeNode* cur = root;
        while(!st.empty() || cur){
            while(cur){
                st.push(cur);
                cur = cur -> left;
            }
            if(!st.empty()){
                cur = st.top();
                st.pop();
                res.emplace_back(cur -> val);
                cur = cur -> right;
            }
        }
        TreeNode* ans = new TreeNode(res[0]);
        cur = ans;
        for(int i = 1; i < res.size(); ++i){
            cur -> right = new TreeNode(res[i]);
            cur = cur -> right;
        }
        return ans;

    }
};