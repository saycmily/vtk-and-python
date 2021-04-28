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
    int rangeSumBST(TreeNode* root, int low, int high) {
        TreeNode* cur = root;
        stack<TreeNode*> st;
        int ans = 0;
        while(!st.empty() || cur){
            while(cur){
                st.push(cur);
                cur = cur -> left;
            }
            if(!st.empty()){
                cur = st.top();
                st.pop();
                if(cur -> val > high)
                    break;
                if(cur->val >= low && cur->val <= high)
                    ans += cur -> val;
                cur = cur -> right; 
            }
        }
        return ans;
    }
};