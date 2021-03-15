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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.size() == 0)
            return nullptr;
        int root = preorder[0];
        int it = find(inorder.begin(), inorder.end(), root) - inorder.begin();
        TreeNode *ans = new TreeNode(root);
        vector<int> leftpre(preorder.begin()+1, preorder.begin()+it+1);
        vector<int> leftino(inorder.begin(), inorder.begin()+it);
        vector<int> rightpre(preorder.begin()+it+1, preorder.end());
        vector<int> rightino(inorder.begin()+it+1, inorder.end());
        ans -> left = buildTree(leftpre, leftino);
        ans -> right = buildTree(rightpre, rightino);
        return ans;
    }
};